from PIL import Image, ImageEnhance

apple = Image.open("apple.jpg")

bw_apple = apple.convert("L")

hc_apple = ImageEnhance.Contrast(apple).enhance(1.4)

bw_apple.save("bw_apple.jpg")

hc_apple.save("hc_apple.jpg")
