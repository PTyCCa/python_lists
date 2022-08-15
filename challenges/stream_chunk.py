"""In the Chunking test, you needed to implement a function that chunks an input sequence (any iterable) into chunks of a given length. In the same test, you will need to do something similar, but with an iterator - potentially infinite! In other words, you have to process the data stream. Examples of such streams are a very large file read from disk or live video data streamed over a network. In both cases, you cannot afford to get all the data at once in the form of a structure in memory - you simply will not have enough. And therefore, you cannot accumulate a list of chunks inside your function, you need to return a stream of chunks.

Implement the ichunks () function, which must take the chunk size (positive integer) and the data source (iterator) as arguments. The function should return an iterator of lists of a given length containing elements from the data source.

Attention, this time you will need to form pieces of a strictly specified length! If there are not enough elements for the last chunk (if the stream ends at all), then the entire chunk is discarded!"""  # noqa E301


def ichunks(size, source):
    return map(list, zip(*([iter(source)] * size)))

# "iter (source)" gets exactly the iterator, even if the input
# iterable (string, list) was passed.
#
# "[iterator] * n" propagates references to the iterator.
#
# "zip (* l)" packs all first elements from
# the list of sources "l", then all the second ones, and so on.
# Since all sources are for zip, these are links to the same
# iterator, when moving from link to link, the cursor moves
# further and further. Therefore, tuples contain consecutive elements.
# --------------------------------------------------------------------
# first try version
# import itertools


# def ichunks(chunk_size, stream):
#     """Enter stream, yield chunks."""
#     iter_stream = iter(stream)
#     while True:
#         chunk = list(itertools.islice(iter_stream, chunk_size))
#         if len(chunk) == chunk_size:
#             yield chunk
#         else:
#             return
