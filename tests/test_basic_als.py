import sys
sys.path.insert(0, './answers')
from answer import basic_als_recommender

def test_basic_als():
    a = basic_als_recommender("./data/sample_movielens_ratings.txt", 123)
    try:
        assert(abs(a-1.62)<0.03)
    except:
        assert(abs(a-1.56)<0.03)
