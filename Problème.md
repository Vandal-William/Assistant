| Type                                                     | Erreurs                                                                                               | Solutions                        |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------- |
| Package: pyaudio                                         | ERROR: Could not build wheels for pyaudio, which is required to install pyproject.toml-based projects | sudo apt install portaudio19-dev |
| Package: pyttsx3                                         | OSError: libespeak.so.1: cannot open shared object file: No such file or directory                    | sudo apt install espeak          |
| command=listener.recognize_google(voix,language='fr-FR') | speech_recognition.UnknownValueError                                                                  |                                  |
