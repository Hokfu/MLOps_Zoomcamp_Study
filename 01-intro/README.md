## Environment Preparation
For developing and automating machine learning models with MLOps practices, Linux environment is important. We have a variety of options.
- AWS EC2
- Cloud Engine ( Google )
- Github CodeSpace

### Using Github CodeSpace
Docker is preinstalled on Github CodeSpace. So, we only need to install Anaconda. In the root directory,

```
wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
bash Anaconda3-2023.09-0-Linux-x86_64.sh
conda install jupyter
```

Check conda path in the environment, we can use this command in the terminal.

```
where conda

```

To define path, first open  `~/.bashrc` file with `nano`. Inside `~/.bashrc`, 

```
export PATH="<YourAnacondaPath>/bin:$PATH"

```

Save it and run the followig to make sure of changes.

```
source ~/.bashrc

```

We can test if we are using the correct interpreter with the following command

```
which python

```

## What I studied

We trained a machine learning model on the [New York Taxi Dataset](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).
In this module, we only practiced maturity 0 model without MLOps asepcts.<br>
#### Data Preparation
We used pick up location ID and drop off location ID and trip distance as features. Our target variable is the trip duration which we got by
substracting pick up datetime from drop off datetime. We get total seconds with `total_seconds()` method to the timedelta object and we divide it by 60 to get total minutes.
<br>
#### Removing Outliers
We can experiment mean, median, mode and standard deviations of trip durations. We can also experiment with the following code. The purpose of the experiments is to detect outliers in the target variable. 

```
df.duration.describe(percentiles=[list])

((df.duration>=1) & (df.duration<=60)).mean()
```

Most of the trips are between 1 minutes and 60 minutes so we removed outliers by only filtering only those trips. <br>
#### Model Training
Regression models such as linear regression, lasso, ridge are trained and validated with `rmse` scores. <br>
## Related Links
- [Module 1 Study Notebook](module1_study.ipynb) | [View on nbviewer](https://nbviewer.org/github/Hokfu/MLOps_Zoomcamp_Study/blob/main/01-intro/module1_study.ipynb)
- [Moduel 1 Homework Notebook](module1_homework.ipynb) | [View on nbviewer](https://nbviewer.org/github/Hokfu/MLOps_Zoomcamp_Study/blob/main/01-intro/module1_homework.ipynb)




