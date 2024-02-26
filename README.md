# FrEsFlashcards

This project aims to automatize the creation of [two-sided flashcards](https://en.wikipedia.org/wiki/Flashcard)

It is possible to change the flashcards' languages by manually editing the code (especially line 10 and line 16)
## How to use:

You **will** need to put a legally acquired Arial Truetype font (**arial.ttf**) in the same folder the program is executed in.
To run this program, you will need to install [deep translator](https://pypi.org/project/deep-translator/), [Faker](https://pypi.org/project/Faker/) and [pillow](https://pypi.org/project/pillow/)
```bash
  pip install deep-translator
  pip install Faker
  pip install pillow
```
Then, you may want to edit line 28 to change the amount of .pdf files that get generated by the program (the default value being 50).
    
## License

This project is licensed under [The Unlicense](https://choosealicense.com/licenses/unlicense/).
