import math
import numpy as np
import xgboost as xgb
from xgboost import plot_importance
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from map import GetDataX, GetDataY


def Prediction(filename, TableName):
    # 读取文件原始数据
    X, y = GetDataY(GetDataX(filename, TableName, 24))

    # XGBoost训练过程
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

    model = xgb.XGBRegressor(max_depth=5, learning_rate=0.1, n_estimators=160, silent=True, objective='reg:gamma')
    model.fit(X_train, y_train)

    # 对测试集进行预测
    ans = model.predict(X_test)
    j = 0
    for i in ans:
        ans[j] = math.floor(ans[j])
        j += 1

    cnt1 = 0
    cnt2 = 0
    for i in range(len(y_test)):
        if ans[i] == y_test[i]:
            cnt1 += 1
        else:
            cnt2 += 1

    print("Accuracy: %.2f %% " % (100 * cnt1 / (cnt1 + cnt2)))
    x = []
    for i in range(32 * 24):
        x.append([i, 2, 2])
    _x = np.asarray(x)
    AnsTest = model.predict(_x)
    j = 0
    for i in AnsTest:
        AnsTest[j] = math.floor(AnsTest[j])
        j += 1
    print(AnsTest)
    # 显示重要特征
    # plot_importance(model)


if __name__ == '__main__':
    name = "数据集.xlsx"
    name_2 = 'default'
    Prediction(name, name_2)
