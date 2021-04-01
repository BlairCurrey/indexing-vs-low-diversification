# [See the analysis here](https://blaircurrey.github.io/indexing-vs-low-diversification/)

## Problem

In some investment circles you often hear statistics such as ["90% of actively managed investment funds failed to beat the market"](https://www.businessinsider.com/personal-finance/investment-pros-cant-beat-the-stock-market-2020-7)
in support of the idea of just buying index funds. For whatever it's worth, I like index funds too and think indexing is a good strategy. But sometimes these statistics are stretched too far to suggest that it's very unlikely that you could beat the market. These are dogmatic indexers. Sometimes it's even implied that this means there is a 10% chance of beating the market. Intuitively this just doesn't make sense.

In response to this idea that an average person has a miniscule chance of beating the market, I ask myself, "If I were to pick 1 stock, isn't there a fair chance that it will beat the market?" Warren Buffet has famously asserted that "diverisification is a protection against ignorance." We may not have the knowledge of Mr. Buffet but we can be confident that minimum portfolio diversity will have a high chance of deviating from the market average. The question at this point is the probablity that it strays in the desired direction.

These claims about beating the market are so common I decided to test the questions I asked myself. My goal is to find this answer for a period of time dating back as far as possible for a set of "normal" companies. The universe of companies is large and their profiles vary. I don't mean finding the next Apple or Amazon, but simply betting on an established, well-known company. Nothing special or complicated. In support of this, I will look at DIA, the oldest mutual fund tracking the Dow Jones, and it's components to see what portion of these outperformed the index as a whole since 1998.

[See the analysis here](https://blaircurrey.github.io/indexing-vs-low-diversification/) and [how I collected the data here](collect-data.ipynb).

## Conclusions

43.33% (13/30) of the companies in the Dow Jones in 1998 beat DIA, the Dow Jones Index, over the same time period, with a median outperformer rising 711.66%, compared to the 549.56% for DIA. Components of the Dow have a standard deviation of 504.07%.

A few of these companies went bankrupt and were delisted. These are represented by `NaN` in our dataframe and are part of the 17 companies that did not beat the average.

This suggests if you were to invest in a Dow Jones company your chance of beating the market is likely much higher than the miniscule 10% sometimes implied by dogmatic indexers.

Instead of suggesting that one's chances of beating the market is necessarily low, I think it's better conclude that most people are not willing to accept the risk of straying from the market average.

### Notes
alternative host for analysis - https://femto.pw/8rmr
