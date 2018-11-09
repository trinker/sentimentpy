sentimentpy
===========

.. image:: bin/sentimentpy_logo/py_sentimentpy.png
    :alt: Module Logo
    

**sentimentpy** is designed to quickly calculate text polarity sentiment at the sentence level and optionally aggregate by rows or grouping variable(s).  


**sentimentpy** (a Python port of the R `sentimentr package <https://github.com/trinker/sentimentr>`_) is a response to my own needs with sentiment detection that were not addressed by the current **R** tools.  My own `polarity` function in the R **qdap** package is slower on larger data sets.  It is a dictionary lookup approach that tries to incorporate weighting for valence shifters (negation and amplifiers/deamplifiers).  Matthew Jockers created the `syuzhet <http://www.matthewjockers.net/2015/02/02/syuzhet>`_ R package that utilizes dictionary lookups for the Bing, NRC, and Afinn methods as well as a custom dictionary.  He also utilizes a wrapper for the `Stanford coreNLP <http://nlp.stanford.edu/software/corenlp.shtml>`_ which uses much more sophisticated analysis.  Jocker's dictionary methods are fast but are more prone to error in the case of valence shifters.  Jocker's `addressed these critiques <http://www.matthewjockers.net/2015/03/04/some-thoughts-on-annies-thoughts-about-syuzhet/>`_ explaining that the method is good with regard to analyzing general sentiment in a piece of literature.  He points to the accuracy of the Stanford detection as well.  In my own work I need better accuracy than a simple dictionary lookup; something that considers valence shifters yet optimizes speed which the Stanford's parser does not.  This leads to a trade off of speed vs. accuracy.  Simply, **sentimentpy** attempts to balance accuracy and speed.