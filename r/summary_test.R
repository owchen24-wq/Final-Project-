df = read.csv("data/clean/final_data.csv")
head(df[order(-df$total_incidents), ], 5)
summary(df$total_incidents)


# quick validity check

df$rate_per_1000 <- 1000 * df$total_incidents / df$pop_2020
head(df[order(-df$rate_per_1000), c("neighborhood", "rate_per_1000")], 10)