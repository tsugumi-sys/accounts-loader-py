from pipelines.nasdaq.pipeline import NASDAQSymbolsPipeline


def main():
    pipeline = NASDAQSymbolsPipeline()
    pipeline.run()


if __name__ == "__main__":
    main()
