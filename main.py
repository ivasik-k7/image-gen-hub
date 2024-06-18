from app.providers import ImageGeneratorContext


def main():
    with ImageGeneratorContext() as client:
        client.generate("xyu")


if __name__ == "__main__":
    main()
