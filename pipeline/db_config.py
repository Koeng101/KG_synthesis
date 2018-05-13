import sqlalchemy
from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,Table,Text,inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

import glob
import json
import pandas as pd

from synbiolib import codon
import itertools

DNA = ['A', 'T', 'G', 'C']
blocks = [''.join(i) for i in itertools.product(DNA, repeat = 5)]

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()


class Oligo(Base):
    '''Describes raw oligo sequences'''
    __tablename__ = 'oligos'

    id = Column(Integer, primary_key=True)
    seq = Column(String) # Holds sequence of the Oligo
    
    # An Oligo can have one block and a Block can have multiple oligos
    block_id = Column(Integer, ForeignKey('block.id'))
    block = relationship("Block", back_populates="oligos")



class Block(Base):
    '''Describes a 5bp block'''
    __tablename__ = 'block'

    id = Column(Integer, primary_key=True)
    seq = Column(String) # Holds 5bp string that the Block corresponds to

    # A Block can have many Oligos and an Oligo can havew one block
    oligos = relationship("Oligo", back_populates="block")


Session = sessionmaker(bind=engine)
Session.configure(bind=engine)


for block in blocks:
    print(block)
