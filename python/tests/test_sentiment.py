import pytest
import mall
import polars as pl
import pyarrow


def test_sentiment_simple():
    data = mall.MallData
    reviews = data.reviews
    reviews.llm.use("test")
    x = reviews.llm.sentiment("review")
    assert (
        x.select("sentiment").to_pandas().to_string()
        == "  sentiment\n0      None\n1      None\n2      None"
    )


def sim_sentiment():
    df = pl.DataFrame(dict(x=["positive", "negative", "neutral", "not-real"]))
    df.llm.use("test")
    return df


def test_sentiment_valid():
    x = sim_sentiment()
    x = x.llm.sentiment("x")
    assert (
        x.select("sentiment").to_pandas().to_string()
        == "  sentiment\n0  positive\n1  negative\n2   neutral\n3      None"
    )


def test_sentiment_valid2():
    x = sim_sentiment()
    x = x.llm.sentiment("x", ["positive", "negative"])
    assert (
        x.select("sentiment").to_pandas().to_string()
        == "  sentiment\n0  positive\n1  negative\n2      None\n3      None"
    )
