import numpy as np    #numpy kutuphanesi vektorlestirme ve program hizlandirma icin
import h5py   #h5 uzantili veri kumsesi dosyasini islemek icin kullanlan kutuphanedir.
def load_dataset():
    train_dataset = h5py.File('train_catvnoncat.h5', "r")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:])
    train_set_y_orig = np.array(train_dataset["train_set_y"][:])
    # training seti yuklendi...
    test_dataset = h5py.File('test_catvnoncat.h5', "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:])
    test_set_y_orig = np.array(test_dataset["test_set_y"][:])
    # test seti yuklendi...
    classes = np.array(test_dataset["list_classes"][:])

    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))
    # setlerini sutun degerlerini garanti olması icin guncelledik...

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes

"""train_set_x_orig , train_set_y , test_set_x_orig , test_set_y , classes = load_dataset()

m_train = train_set_y.shape[1]
m_test = test_set_y.shape[1]
num_px = train_set_x_orig.shape[1]
### END CODE HERE ###

print ("Eğitim örneği adedi : m_train = " + str(m_train))
print ("Test örneklerinin adedi : m_test = " + str(m_test))
print ("Her görüntünün yükseklik ve genişlik değeri : num_px = " + str(num_px))
print ("Her görüntünün boyutu : (" + str(num_px) + ", " + str(num_px) + ", 3)")
print ("train_set_x shape : " + str(train_set_x_orig.shape))
print ("train_set_y shape : " + str(train_set_y.shape))
print ("test_set_x shape : " + str(test_set_x_orig.shape))
print ("test_set_y shape : " + str(test_set_y.shape))"""