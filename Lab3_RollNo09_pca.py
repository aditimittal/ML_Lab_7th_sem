from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np
from statistics import mean,stdev
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn import cross_validation
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
def mat_transpose(X):
	result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
	return result
def dot_prod(X,Y):
	result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
	return result
#read data from file
file='diabetes.xlsx'
x1=pd.ExcelFile(file)
df1=pd.read_excel(x1,'diabetes')
df1=df1.rename(columns={'first_prop':'first_prop', 'second_prop':'second_prop','third_prop':'third_prop','fourth_prop':'fourth_prop','fifth_prop':'fifth_prop','sixth_prop':'sixth_prop','seventh_prop':'seventh_prop', 'eighth_prop':'eighth_prop', 'ninth_prop':'ninth_prop'})
first_changed=[]
second_changed=[]
third_changed=[]
fourth_changed=[]
fifth_changed=[]
sixth_changed=[]
seventh_changed=[]
eighth_changed=[]
#find mean for every column
first_prop_mean=mean(df1.first_prop)
second_prop_mean=mean(df1.second_prop)
third_prop_mean=mean(df1.third_prop)
fourth_prop_mean=mean(df1.fourth_prop)
fifth_prop_mean=mean(df1.fifth_prop)
sixth_prop_mean=mean(df1.sixth_prop)
seventh_prop_mean=mean(df1.seventh_prop)
eighth_prop_mean=mean(df1.eighth_prop)
#subtract mean from data for every feature
for i in df1.first_prop:
	i=i-first_prop_mean
	first_changed.append(i)
for i in df1.second_prop:
	i=i-second_prop_mean
	second_changed.append(i)
for i in df1.third_prop:
	i=i-third_prop_mean
	third_changed.append(i)
for i in df1.fourth_prop:
	i=i-fourth_prop_mean
	fourth_changed.append(i)
for i in df1.fifth_prop:
	i=i-fifth_prop_mean
	fifth_changed.append(i)
for i in df1.sixth_prop:
	i=i-sixth_prop_mean
	sixth_changed.append(i)
for i in df1.seventh_prop:
	i=i-seventh_prop_mean
	seventh_changed.append(i)
for i in df1.eighth_prop:
	i=i-eighth_prop_mean
	eighth_changed.append(i)
#find covariance matrix for the eight features
cov_mat = np.cov([df1.first_prop,df1.second_prop,df1.third_prop,df1.fourth_prop,df1.fifth_prop,df1.sixth_prop,df1.seventh_prop,df1.eighth_prop])
print cov_mat
mat=np.array([[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,1]])
#find the eigen values and eigen vectors for the matrix
eig_val_cov, eig_vec_cov = np.linalg.eig(cov_mat)
print "\n\n\n"
for i in range(len(eig_val_cov)):
	eigvec_cov=np.array(mat_transpose(eig_vec_cov[:,i].reshape(1,8)))

eig_pairs = [(np.abs(eig_val_cov[i]), eig_vec_cov[:,i]) for i in range(len(eig_val_cov))]
#sort the eigen vectors according to the decreasing order of the eigen values
eig_pairs.sort(key=lambda x: x[0], reverse=True)

# Visually confirm that the list is correctly sorted by decreasing eigenvalues
for i in eig_pairs:
    print(i[0])
#create matrix which can transform the dimensions to only two dimensions
matrix_w = np.hstack((eig_pairs[0][1].reshape(8,1), eig_pairs[1][1].reshape(8,1)))
print('Matrix W:\n', matrix_w)
#transformed data
transformed = np.array(dot_prod(np.array(mat_transpose(matrix_w)),([df1.first_prop,df1.second_prop,df1.third_prop,df1.fourth_prop,df1.fifth_prop,df1.sixth_prop,df1.seventh_prop,df1.eighth_prop])))
print transformed
features = ["first_prop","second_prop","third_prop","fourth_prop","fifth_prop","sixth_prop","seventh_prop", "eighth_prop"]
target = "ninth_prop"

properties=[0,1]
transformed = np.array(mat_transpose(transformed))
df2=pd.DataFrame.from_records(transformed)
features_train, features_test, target_train, target_test = cross_validation.train_test_split(df2,df1.ninth_prop,test_size=0.1, random_state=7)
#applying gaussian after pca
model = GaussianNB()
model.fit(features_train, target_train)
pred = model.predict(features_test)
accuracy = accuracy_score(target_test, pred)
print "accuracy of the model after pca is "+str(accuracy)

#applying gaussian before pca
features_train, features_test, target_train, target_test = cross_validation.train_test_split(df1[features],df1.ninth_prop,test_size=0.1, random_state=7)
model = GaussianNB()
model.fit(features_train, target_train)
pred = model.predict(features_test)
accuracy = accuracy_score(target_test, pred)
print "accuracy of the model before pca is "+str(accuracy)