# Task 1
# String of book "Wuthering Heights"
book_text = """CHAPTER I
1801 I have just returned from a visit to my landlord the solitary
neighbour that I shall be troubled with. This is certainly a beautiful
country! In all England, I do not believe that I could have fixed on a
situation so completely removed from the stir of society. A perfect
misanthropist s Heaven and Mr. Heathcliff and I are such a suitable
pair to divide the desolation between us. A capital fellow! He little
imagined how my heart warmed towards him when I beheld his black eyes
withdraw so suspiciously under their brows, as I rode up, and when his
fingers sheltered themselves, with a jealous resolution, still further
in his waistcoat, as I announced my name.

Mr. Heathcliff? I said.

A nod was the answer.

Mr. Lockwood, your new tenant, sir. I do myself the honour of calling
as soon as possible after my arrival, to express the hope that I have
not inconvenienced you by my perseverance in soliciting the occupation
of Thrushcross Grange: I heard yesterday you had had some thoughts 

Thrushcross Grange is my own, sir, he interrupted, wincing. I should
not allow any one to inconvenience me, if I could hinder it walk in!

The walk in was uttered with closed teeth, and expressed the
sentiment, Go to the Deuce! even the gate over which he leant
manifested no sympathising movement to the words; and I think that
circumstance determined me to accept the invitation: I felt interested
in a man who seemed more exaggeratedly reserved than myself.

When he saw my horse s breast fairly pushing the barrier, he did put
out his hand to unchain it, and then sullenly preceded me up the
causeway, calling, as we entered the court, Joseph, take Mr.
Lockwood s horse; and bring up some wine.

Here we have the whole establishment of domestics, I suppose, was the
reflection suggested by this compound order. No wonder the grass grows
up between the flags, and cattle are the only hedge cutters.

Joseph was an elderly, nay, an old man, very old, perhaps, though hale
and sinewy. The Lord help us! he soliloquised in an undertone of
peevish displeasure, while relieving me of my horse: looking, meantime,
in my face so sourly that I charitably conjectured he must have need of
divine aid to digest his dinner, and his pious ejaculation had no
reference to my unexpected advent.

Wuthering Heights is the name of Mr. Heathcliff s dwelling. Wuthering
being a significant provincial adjective, descriptive of the
atmospheric tumult to which its station is exposed in stormy weather.
Pure, bracing ventilation they must have up there at all times, indeed:
one may guess the power of the north wind, blowing over the edge, by
the excessive slant of a few stunted firs at the end of the house; and
by a range of gaunt thorns all stretching their limbs one way, as if
craving alms of the sun. Happily, the architect had foresight to build
it strong: the narrow windows are deeply set in the wall, and the
corners defended with large jutting stones.
"""

# Task 2
# text from stopwords in github
_stop_words_text = """
a
about
above
after
again
against
all
also
am
an
and
any
are
aren't
as
at
be
because
been
before
being
below
between
both
but
by
can
can't
cannot
com
could
couldn't
did
didn't
do
does
doesn't
doing
don't
down
during
each
else
ever
few
for
from
further
get
had
hadn't
has
hasn't
have
haven't
having
he
he'd
he'll
he's
hence
her
here
here's
hers
herself
him
himself
his
how
how's
however
http
i
i'd
i'll
i'm
i've
if
in
into
is
isn't
it
it's
its
itself
just
k
let's
like
me
more
most
mustn't
my
myself
no
nor
not
of
off
on
once
only
or
other
otherwise
ought
our
ours
ourselves
out
over
own
r
same
shall
shan't
she
she'd
she'll
she's
should
shouldn't
since
so
some
such
than
that
that's
the
their
theirs
them
themselves
then
there
there's
therefore
these
they
they'd
they'll
they're
they've
this
those
through
to
too
under
until
up
very
was
wasn't
we
we'd
we'll
we're
we've
were
weren't
what
what's
when
when's
where
where's
which
while
who
who's
whom
why
why's
with
won't
would
wouldn't
www
you
you'd
you'll
you're
you've
your
yours
yourself
yourselves
"""
# Make a list for stop words
# formated
# help from https://www.digitalocean.com/community/tutorials/python-convert-string-to-list
stop_words = [w.strip().lower() for w in _stop_words_text.splitlines() if w.strip()]

# Task 3
# Some extra stop words
extra_stop_words = [
    "mr", "sir", "said", "one", "two", "would", "could", "might", "s",
    "shall", "thrushcross", "grange", "wuthering", "heathcliff", "lockwood"
]

# Characters to remove (we ll replace these with spaces)
chars_to_remove = [
    "_", "*", ".", ",", "!", "?", ":", ";", "(", ")", "[", "]", "{", "}", '"', "'", "\n", "\t"
]

#Lowercase, remove punctuation, split into words, and remove stop words.
def get_clean_words(text: str) -> list[str]:
    #Lowercase
    text = text.lower()

    # remove punctuation
    for ch in chars_to_remove:
        text = text.replace(ch, " ")

    # split
    words = text.split()

    # Remove stop words
    all_stops = set(stop_words) | set(extra_stop_words)
    cleaned_list = [w for w in words if w not in all_stops and not w.isdigit()]

    return cleaned_list