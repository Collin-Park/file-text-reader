# file-text-reader

a weekend project craping web data for some financial information,
the USD AUD pair is retrieved from yahoo and appended to the CSV,
I am looking at automating the program process for a daily retrieval. (something like cron for unix, unfortunately I'm on windows)

For future use of this tool, I hope to be able to scrape the web en masse (without directing to specific urls) for less polished data.

when the program analyze_from_request.py is run, the csv, USDAUD_exchange_rate.csv is updated with the date, 52 week low, high and current value.

in other files, there are ways to request an html and save it as a html file, there is a way to analyze and parse html files from an html file.
