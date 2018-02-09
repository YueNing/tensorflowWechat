import numpy as np

class MultinomialNB(object):
    def __init__(self, alpha=1.0, fit_prior=True, class_prior=None):
        self.alpha = alpha
        self.fit_priori = fit_prior
        self.calss_prior = class_prior
        self.classes = None
        self.conditional_prob = None


    def _calculat_feature_prob(self, feature):
        values = np.unique(feature)
        total_num = float(len(feature))
        value_prob = {}
        for v in values:
            value_prob[v] = ((np.sum(np.equal(feature, v)) + self.alpha) / (total_num + len(values) * self.alpha))
        return value_prob

    def fit(self, X, y):

        self.classes = np.unique(y)
        if self.calss_prior == None:
            class_num = len(self.classes)
            if not self.fit_prior:
                self.class_prior = [1.0 / class_num for _ in range(class_num)]
            else:
                self.class_prior = []
