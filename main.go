package main

import (
	"flag"
	"fmt"
	"github.com/ojrac/opensimplex-go"
	"image"
	"image/color"
	"image/gif"
	"image/jpeg"
	"image/png"
	"log"
	"math"
	"math/rand"
	"os"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixMilli())
	width, height, target, targetType, seed, length := parseArgs()

	// initialized the randomizer with the passed seed to enable deterministic outputs
	log.Printf("Generating image with the following seed: %d", seed)
	rand.Seed(seed)

	// smaller = smoother, larger = rougher
	roughness := (1 + rand.Float64()*2) / float64(width)

	switch targetType {
	case "png":
		f, err := os.OpenFile(target, os.O_WRONLY|os.O_CREATE, 0644)
		if err != nil {
			log.Fatal(err)
		}

		img := generateNRGBAImage(width, height, seed, roughness, 0)
		err = png.Encode(f, img)
		if err != nil {
			log.Fatal(err)
		}

		err = f.Close()
		if err != nil {
			log.Fatal(err)
		}
	case "jpg", "jpeg":
		f, err := os.OpenFile(target, os.O_WRONLY|os.O_CREATE, 0644)
		if err != nil {
			log.Fatal(err)
		}

		img := generateNRGBAImage(width, height, seed, roughness, 0)
		err = jpeg.Encode(f, img, &jpeg.Options{Quality: jpeg.DefaultQuality})
		if err != nil {
			log.Fatal(err)
		}

		err = f.Close()
		if err != nil {
			log.Fatal(err)
		}
	case "gif":
		f, err := os.OpenFile(target, os.O_WRONLY|os.O_CREATE, 0644)
		if err != nil {
			log.Fatal(err)
		}

		// TODO: animation
		img := generateNRGBAImage(width, height, seed, roughness, 0)
		err = gif.Encode(f, img, &gif.Options{NumColors: 256})
		if err != nil {
			log.Fatal(err)
		}

		err = f.Close()
		if err != nil {
			log.Fatal(err)
		}
	case "pitft":
		f, err := os.OpenFile(target, os.O_WRONLY, 0644)
		if err != nil {
			log.Fatal(err)
		}

		img := generatePiTFTImage(width, height, seed, roughness, 0)
		bytes := convertImageToPiTFTBytes(img)
		_, err = f.Write(bytes)
		if err != nil {
			log.Fatal(err)
		}

		err = f.Close()
		if err != nil {
			log.Fatal(err)
		}
	case "pitft-animated":
		f, err := os.OpenFile(target, os.O_WRONLY, 0644)
		if err != nil {
			log.Fatal(err)
		}

		for i := 1; i <= length; i++ {
			img := generatePiTFTImage(width, height, seed, roughness, i)
			bytes := convertImageToPiTFTBytes(img)

			_, err = f.Seek(0, 0)
			if err != nil {
				log.Fatal(err)
			}
			_, err = f.Write(bytes)
			if err != nil {
				log.Fatal(err)
			}
		}

		err = f.Close()
		if err != nil {
			log.Fatal(err)
		}
	default:
		fmt.Printf("Unsupported format '%s'", targetType)
		os.Exit(1)
	}
}

// all the floats returned by the returned function are between 0 and 1
func getNoiseFunc(seed int64, roughness float64, offset int) func(x int, y int) (float64, float64, float64, float64) {
	rNoise := opensimplex.New(seed)
	gNoise := opensimplex.New(seed + 1)
	bNoise := opensimplex.New(seed + 2)
	aNoise := opensimplex.New(seed + 3)

	return func(x int, y int) (float64, float64, float64, float64) {
		return rNoise.Eval3(float64(x)*roughness, float64(y)*roughness, float64(offset)*0.02),
			gNoise.Eval3(float64(x)*roughness, float64(y)*roughness, float64(offset)*0.02),
			bNoise.Eval3(float64(x)*roughness, float64(y)*roughness, float64(offset)*0.02),
			aNoise.Eval3(float64(x)*roughness, float64(y)*roughness, float64(offset)*0.02)
	}
}

func generateNRGBAImage(width int, height int, seed int64, roughness float64, offset int) *image.NRGBA {
	// fill the image with data from the noises
	noiseFunc := getNoiseFunc(seed, roughness, offset)
	img := image.NewNRGBA(image.Rect(0, 0, width, height))
	for x := 0; x < width; x++ {
		for y := 0; y < height; y++ {
			r, g, b, a := noiseFunc(x, y)
			img.Set(x, y, color.NRGBA{
				R: uint8(math.Abs(r * 255)),
				G: uint8(math.Abs(g * 255)),
				B: uint8(math.Abs(b * 255)),
				// we limit alpha to the lower 6 bits of randomness to keep it above a certain level
				A: uint8(math.Abs(a*63)) + 192,
			})
		}
	}

	return img
}

func generatePiTFTImage(width int, height int, seed int64, roughness float64, offset int) *image.NRGBA {
	// fill the image with data from the noises
	noiseFunc := getNoiseFunc(seed, roughness, offset)
	img := image.NewNRGBA(image.Rect(0, 0, width, height))
	for x := 0; x < width; x++ {
		for y := 0; y < height; y++ {
			r, g, b, _ := noiseFunc(x, y)
			img.Set(x, y, color.NRGBA{
				R: uint8(math.Abs(r * 31)),
				G: uint8(math.Abs(g * 63)),
				B: uint8(math.Abs(b * 31)),
				A: 0,
			})
		}
	}

	return img
}

func convertImageToPiTFTBytes(img *image.NRGBA) []byte {
	bytes := make([]byte, len(img.Pix)/2)

	offset := int64(0)
	byteCnt := 0
	var r, g, b uint8
	for _, pix := range img.Pix {
		byteCnt++
		switch byteCnt {
		case 1:
			r = pix
			continue
		case 2:
			g = pix
			continue
		case 3:
			b = pix
			continue
		}
		byteCnt = 0

		// The TFT screen uses two bytes per pixel in the following format:
		// gggbbbbb rrrrrggg
		bytes[offset] = b
		bytes[offset] |= g << 5
		bytes[offset+1] = g >> 3
		bytes[offset+1] |= r << 3
		offset += 2
	}

	return bytes
}

func parseArgs() (int, int, string, string, int64, int) {
	var width, height, length int
	var output, outputType string
	var seed int64

	flag.IntVar(&width, "width", 800, "The width of the target image")
	flag.IntVar(&height, "height", 800, "The height of the target image")
	flag.StringVar(&output, "output", "DEFAULT", "The target file")
	flag.StringVar(&outputType, "type", "png", "The target file")
	flag.Int64Var(&seed, "seed", rand.Int63(), "The seed for the image generation")
	flag.IntVar(&length, "length", 10, "How long the animation should be (ignored on non-animated images).")
	flag.Parse()

	if output == "DEFAULT" {
		output = fmt.Sprintf("./randomImage-%d-%d.%s", width, height, outputType)
	}

	return width, height, output, outputType, seed, length
}
