from PIL import Image, ImageDraw

__PATH_TO_REFERENCE_SCREENSHOTS = "screenshots/reference/"
__PATH_TO_ACTUAL_SCREENSHOTS = "screenshots/actual/"
__PATH_TO_SCREENSHOTS = "screenshots/"


def compare_screenshots(reference_screenshot_name, actual_screenshot_name, result_screenshot_name):
    reference_screenshot = Image.open(__PATH_TO_REFERENCE_SCREENSHOTS + reference_screenshot_name)
    actual_screenshot = Image.open(__PATH_TO_ACTUAL_SCREENSHOTS + actual_screenshot_name)
    columns = 40
    rows = 200
    screen_width, screen_height = reference_screenshot.size

    block_width = ((screen_width - 1) // columns) + 1
    block_height = ((screen_height - 1) // rows) + 1

    for y in range(0, screen_height, block_height + 1):
        for x in range(0, screen_width, block_width + 1):
            region_sample = _process_region(reference_screenshot, x, y, block_width, block_height)
            region_tested = _process_region(actual_screenshot, x, y, block_width, block_height)

            if region_sample is not None and region_tested is not None and region_tested != region_sample:
                draw = ImageDraw.Draw(actual_screenshot)
                draw.rectangle((x, y, x + block_width, y + block_height), outline="red")

    actual_screenshot.save(__PATH_TO_SCREENSHOTS + result_screenshot_name)


def _process_region(image, x, y, width, height):
    region_total = 0
    factor = 100

    for coordinateY in range(y, y + height):
        for coordinateX in range(x, x + width):
            try:
                pixel = image.getpixel((coordinateX, coordinateY))
                region_total += sum(pixel) / 4
            except:
                return

    return region_total/factor
