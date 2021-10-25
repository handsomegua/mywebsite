knitr::opts_chunk$set(echo = TRUE)
library(plotly)
library(tidyquant)
sm_df<- read.csv('sm_final_output.csv')
fig <- plot_ly(sm_df, type = 'scatter', mode = 'lines')%>%
  add_trace(x = ~Time, y = ~powerallphases,split = ~House)%>%
  layout(showlegend = F, title='Time Series with Range Slider and Selectors in each Household',
         xaxis = list(rangeslider = list(visible = T),
                      rangeselector=list(
                        buttons=list(
                          list(count=1, label="1h", step="hour", stepmode="backward"),
                          list(count=6, label="6h", step="hour", stepmode="backward"),
                          list(count=1, label="1D", step="day", stepmode="todate"),
                          list(count=1, label="1M", step="month", stepmode="backward"),
                          list(step="all")
                        ))))
fig <- fig %>%
  layout(
    xaxis = list(zerolinecolor = '#ffff',
                 zerolinewidth = 2,
                 gridcolor = 'ffff'),
    yaxis = list(zerolinecolor = '#ffff',
                 zerolinewidth = 2,
                 gridcolor = 'ffff'),
    plot_bgcolor='#e5ecf6', margin = 0.1, width = 900)
fig

htmlwidgets::saveWidget(as_widget(fig), "plotly.html")
