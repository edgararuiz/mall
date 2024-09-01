
<!-- README.md is generated from README.Rmd. Please edit that file -->

# mall

<!-- badges: start -->
<!-- badges: end -->

Adds the ability to batch LLM predictions that run row wise on the data.
The predictions made are based on pre-specified prompts that will
perform the following:

- Sentiment analysis
- Summarize the text
- Extract one, or several, specific pieces information from the text

There will be more added in the future.

This package is inspired by the SQL AI functions now offered by vendors
such as Databricks and Snowflake.

For local data, `mall` uses Ollama to interact with a locally installed
LLM. If using with Databricks, `mall` will use SQL to access their AI
functions.

## Usage

``` r
library(dplyr)
library(mall)

reviews  <- tribble(
  ~ review,
    "This has been the best TV I've ever used. Great screen, and sound.", 
    "I regret buying this laptop. It is too slow and the keyboard is too noisy", 
    "Not sure how to feel about my new washing machine. Great color, but hard to figure"
  )
```

``` r
reviews |>
  llm_sentiment(review)
#> Ollama local server running
#> # A tibble: 3 × 2
#> 1 This has been the best TV I've ever use… positive
#> 2 I regret buying this laptop. It is too … negative
#> 3 Not sure how to feel about my new washi… neutral
```

``` r
reviews |>
  llm_sentiment(review, options = c("positive", "negative"))
#> # A tibble: 3 × 2
#> 1 This has been the best TV I've ever use… positive
#> 2 I regret buying this laptop. It is too … negative
#> 3 Not sure how to feel about my new washi… negative
```

``` r
reviews |>
  llm_extract(review, "product")
#> # A tibble: 3 × 2
#> 1 This has been the best TV I've ever use… tv             
#> 2 I regret buying this laptop. It is too … laptop         
#> 3 Not sure how to feel about my new washi… washing machine
```

``` r
reviews |> 
  llm_summarize(review, max_words = 5) 
#> # A tibble: 3 × 2
#> 1 This has been the best TV I've ever use… very good tv performance overall
#> 2 I regret buying this laptop. It is too … laptop is too slow noisy        
#> 3 Not sure how to feel about my new washi… new washing machine not perfect
```
