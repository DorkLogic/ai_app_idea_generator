import sys
import pkg_resources

def test_imports():
    libraries = [
        'requests', 'pandas', 'numpy', 'pytrends', 'tweepy', 'praw',
        'nltk', 'spacy', 'gensim', 'openai', 'scipy'
    ]
    
    for lib in libraries:
        try:
            imported_lib = __import__(lib)
            version = pkg_resources.get_distribution(lib).version
            print(f"{lib} version {version} imported successfully!")
        except ImportError as e:
            print(f"Error importing {lib}: {str(e)}")
        except Exception as e:
            print(f"Unexpected error with {lib}: {str(e)}")
    
    # Detailed check for scipy
    try:
        import scipy
        print(f"scipy version: {scipy.__version__}")
        from scipy import linalg
        print("scipy.linalg imported successfully!")
        triu = linalg.triu
        print("scipy.linalg.triu function accessed successfully!")
        
        # Test triu function
        import numpy as np
        test_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        result = triu(test_matrix)
        print("triu function test result:")
        print(result)
        
    except ImportError as e:
        print(f"Error importing or using scipy.linalg.triu: {str(e)}")
    except Exception as e:
        print(f"Unexpected error with scipy.linalg.triu: {str(e)}")

if __name__ == "__main__":
    print(f"Python version: {sys.version}")
    test_imports()
