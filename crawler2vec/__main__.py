import asyncio
from itertools import product
from crawler2vec.datasource import alias as datasources
from crawler2vec.vectorizer import alias as vectorizers
from crawler2vec.datadestination import alias as datadestinations
from crawler2vec.abc import run
from argparse import ArgumentParser


def func_parser_gen(datasource_constructor, vectorizer_constructor, datadestination_constructor):
    def func_parser(parser):
        args = parser.parse_args()
        datasource = datasource_constructor(args)
        vectorizer = vectorizer_constructor(args)
        datadestination = datadestination_constructor(args)
        asyncio.get_event_loop().run_until_complete(
            run(datasource, vectorizer, datadestination, batch_size=args.batch_size)
        )
    return func_parser


parser = ArgumentParser()
subparsers = parser.add_subparsers(help='sub-command help')
for datasource, vectorizer, datadestination in product(datasources.keys(), vectorizers.keys(), datadestinations.keys()):
    subparser = subparsers.add_parser(
        f"{datasource}-{vectorizer}-{datadestination}",
        help=f"{datasource} -text-> {vectorizer} -vector-> {datadestination}"
    )
    datasources[datasource].add_arguements(subparser)
    vectorizers[vectorizer].add_arguements(subparser)
    datadestinations[datadestination].add_arguements(subparser)
    subparser.set_defaults(func=func_parser_gen(
        datasources[datasource],
        vectorizers[vectorizer],
        datadestinations[datadestination]
    ))


# --------- Run ---------
args = parser.parse_args()
args.func(parser)
