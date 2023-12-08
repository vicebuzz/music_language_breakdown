# Project to identify language of songs in my library and present a language breakdown

## Plan
- Scrape songs from apple music
- Train an NLP model to identify a language of each of the songs
- Dump everything in CSV file or RDBMS
- Go through records, correcting mistakes
- Create visualisation panels (perhaps only one)

## Resources used
* [Tunemymusic](https://www.tunemymusic.com/) -> used it to scrape music and turn and get it as a CSV file
* [Spark](https://spark.apache.org/) -> Python NLP library to present base for nlp pipeline to detect text language.
* [JonhSnowLabs](https://demo.johnsnowlabs.com/public/LANGUAGE_DETECTOR) -> spark extension presenting NLP pipeline to detect the text language
* [MusicBrainz](https://picard.musicbrainz.org/) -> Possible last resort to validate song language.

## Description
This project was inspired by GitHub breakdown of programming languages in the repository. Initial idea is to scrape song names and details from user library, followed by training an NLP model to detect the language of their title. After language of the title is detected, the label is assigned. However, after looking at the dataset of music from my library, a few question come to mind. First of all, what if song title isn't text at all? It may be numbers or some symbols or perhaps, individual letters. Examples that come to mind are 2+2=5 by Radiohead or 1 2 X U by Wire. This makes identification of song language by title impossible. However, we may bring an artist name into equation and see what language they generally sing in. The same really goes to the next question, which is what if the song title is written in one language, such as English, however the song is actually sang in other language, Russian for example. 

The last resort after checking the language of artist name, song title and album title can API reference to MusicBrainz digital music library - where language, even multiple are listed for each song.

Bilingual songs are also a concert to overall accuracy, but spliting song length into various lingvistically unique parts would require research of song's lyrics and verse to position in the song time series. At the momement, the point is to provide percentage breakdown of songs in the music library, rather than breakdown of actual song length.

Another present challenge is the absence of labled data to see model accuracy. As after initial run, with dataset aimed at identifing 315 languages, there are more errors, than on the model with dataset aimed at identifing only 43 languages. And manual identification of each song's language is a tidious and time-exhausting process. 

## Project implementation steps taken

### Stage 1 - intial testing and error validation

[imgs/initial_result.png] - Result of language breakdown after first model run

Thngs that can be spotted straigt away is the large number of unknown values and wide range of languages detected. This is a sign of model overfitting and making results innacurate. Even though the dataset that was chosen is not the biggest in terms of languages it is able to detect, only 43, compared to 315 or 299, available there. For example, there were 8 hungarian songs detected, even though I believe only have a few, maximum 3 in my playlist. Same goes to 17 latin songs detected out of nowhere. Even some clearly English songs like Overdrive or Overcome were not labeled as English, instead as Unknown.