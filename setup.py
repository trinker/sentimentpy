setup(
  name = 'sentimentpy',
  #packages = ['vaderSentiment'], # this must be the same as the name above
  packages = find_packages(exclude=['tests*']), # a better way to do it than the line above -- this way no typo/transpo errors
  include_package_data=True,
  version = '2.7.0',
  description = 'sentimentpy: Calculate Text Polarity Sentiment',
  long_description = read("README.rst"),
  long_description_content_type = 'text/markdown',
  author = 'Tyler W. Rinker',
  author_email = 'tyler.rinker@gmail.com',
  license = 'MIT License: http://opensource.org/licenses/MIT',
  url = 'https://github.com/cjhutto/vaderSentiment', # use the URL to the github repo
  download_url = 'https://github.com/trinker/sentimentpy/archive/master.zip', 
  keywords = ['sentiment'], # arbitrary keywords
  classifiers = ['Development Status :: 4 - Beta', 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: MIT License', 'Natural Language :: English',
                 'Programming Language :: Python :: 3.6', 'Topic :: Scientific/Engineering :: Artificial Intelligence',
                 'Topic :: Scientific/Engineering :: Information Analysis', 'Topic :: Text Processing :: Linguistic',
                 'Topic :: Text Processing :: General'],
)