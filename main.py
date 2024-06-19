from app.providers import ImageGeneratorContext


def main():
    with ImageGeneratorContext() as client:
        client.generate(
            "fancy red brown toy poodle raiding an survivalist post apocalypse car",
            **{
                "height": 1024,
                "width": 1024,
            },
        )


if __name__ == "__main__":
    main()
