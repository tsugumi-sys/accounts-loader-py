# from pipelines.nasdaq.pipeline import NASDAQSymbolsPipeline
from data_loaders.nasdaq.data_loader import AMEXSymbolsDataLoader


def main():
    # pipeline = NASDAQSymbolsPipeline()
    # pipeline.run()

    data_loader = AMEXSymbolsDataLoader()
    repo = data_loader.download()
    print(repo.list_artifacts())

    # repo = LocalArtifactRepository("test_repo")
    # repo.log_artifact("./financials.csv")
    # print(repo.artifact_dir)
    # print(repo.list_artifacts()[0])


if __name__ == "__main__":
    main()
