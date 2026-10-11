# ---------- Base Class ----------
class Instrument:
    def play(self):
        raise NotImplementedError("Subclass must implement the play() method")


# ---------- Subclasses ----------
class Guitar(Instrument):
    def play(self):
        print("Strumming the guitar")


class Piano(Instrument):
    def play(self):
        print("Pressing the keys on the piano")


# ---------- Polymorphism Function ----------
def make_instrument_play(instrument):
    instrument.play()


# ---------- Demonstration ----------
guitar = Guitar()
piano = Piano()

make_instrument_play(guitar)
make_instrument_play(piano)

# Base class সরাসরি ব্যবহার করলে কী হয়
print("\n--- Base class টেস্ট ---")
try:
    make_instrument_play(Instrument())
except NotImplementedError as e:
    print("Error:", e)