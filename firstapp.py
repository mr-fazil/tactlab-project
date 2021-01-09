from flask import Flask, jsonify, request, redirect
from flask_pymongo import PyMongo
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://fazil123:fazil123@cluster0.ml7sf.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
db_enter = db.test


@app.route('/create-many')
def create_many():
    new_user_1 = {'1-10 Tips to learn Machine Learning effectively':'https://atharvaaingle.medium.com/10-tips-to-learn-machine-learning-72b7dcf15528'}
    new_user_2 = {'2-A Beginner’s Guide to Machine Learning' :'https://medium.com/@randylaosat/a-beginners-guide-to-machine-learning-dfadc19f6caf'}
    new_user_3 = {'3-Apple’s New M1 Chip is a Machine Learning Beast' :'https://towardsdatascience.com/apples-new-m1-chip-is-a-machine-learning-beast-70ca8bfa6203'}
    new_user_4 = {'4-How To Become A Computer Vision Engineer In 2021' :'https://towardsdatascience.com/how-to-become-a-computer-vision-engineer-in-2021-c563545d4c9a'}
    new_user_5 = {'5-What French Bread Teaches Us About Artificial Intelligence (AI) And Machine Learning (ML)' :'https://johnmaeda.medium.com/what-french-bread-teaches-us-about-artificial-intelligence-ai-and-machine-learning-ml-6865db2a8331'}
    new_user_6 = {'6-The Non-Technical Guide to Machine Learning & Artificial Intelligence' :'https://machinelearnings.co/a-humans-guide-to-machine-learning-e179f43b67a0'}
    new_user_7 = {'7-Using machine learning to analyse qualitative survey data' :'https://towardsdatascience.com/using-machine-learning-to-analyse-qualitative-survey-data-1794416e5474'}
    new_user_8 = {'8-Machine Learning in Rust, Logistic Regression' :'https://volodymyr-orlov.medium.com/machine-learning-in-rust-logistic-regression-74d6743df161'}
    new_user_9 = {'9-Using Machine Learning to Predict Price of Product on Mercari' :'https://medium.com/swlh/using-machine-learning-to-predict-price-of-product-on-mercari-461ee174d94e'}
    new_user_10 = {'10-How to Solve ML’s Reproducibility Crisis in 3 Easy Steps' :'https://towardsdatascience.com/addressing-mls-reproducibility-crisis-7d59e9ed050'}
    new_user_11 = {'11-PassGAN: A Deep Learning Approach to Password Guessing' :'https://sam-thurman.medium.com/passgan-a-deep-learning-approach-to-password-guessing-df2bbc799904'}
    new_user_12 = {'12-Why Robustness is not Enough for Safety and Security in Machine Learning' :'https://ckaestne.medium.com/why-robustness-is-not-enough-for-safety-and-security-in-machine-learning-1a35f6706601'}
    new_user_13 = {'13-Discrete Probability Distributions for Machine Learning' :'https://medium.com/codex/discrete-probability-distributions-for-machine-learning-90fae177b73'}
    new_user_14 = {'14-Image Processing, Computer Vision, Machine Learning With OpenCV' :'https://medium.com/analytics-vidhya/image-processing-computer-vision-machine-learning-with-opencv-cdde5cd24267'}
    new_user_15 = {'15-DeepMind’s protein folding solution — what just happened?' :'https://medium.com/cgo-benchmark/deepminds-protein-folding-solution-what-just-happened-279d32e8d0f'}
    new_user_16 = {'16-Popular Machine Learning Performance Metrics' :'https://towardsdatascience.com/popular-machine-learning-performance-metrics-a2c33408f29'}
    new_user_17 = {'17-Interpretable Machine Learning — A Short Survey' :'https://maulik-parmar.medium.com/interpretable-machine-learning-a-short-survey-bb7b5ace7ae6'}
    new_user_18 = {'18-Mathematics and Statistics behind Machine Learning — PART 1' :'https://medium.com/analytics-vidhya/mathematics-and-statistics-behind-machine-learning-part-1-eede0e152d57'}
    new_user_19 = {'19-My Top 3 Machine Learning Algorithms' :'https://towardsdatascience.com/my-top-3-machine-learning-algorithms-7eaa19d9bb36'}
    new_user_20 = {'20-Machine Learning and Generalization Error — Is Learning Possible?' :'https://najamogeltoft.medium.com/machine-learning-and-generalization-error-is-learning-possible-cff8721285e0'}
    new_user_21 = {'21-Using Machine Learning to Classify Server Incidents' :'https://caiopedroso-data-ai.medium.com/using-machine-learning-to-classify-server-incidents-36f837c107a'}
    new_user_22 = {'22-ML Apps using dstack ai' :'https://towardsdatascience.com/ml-apps-using-dstack-ai-953d20a489b'}
    new_user_23 = {'23-Machine Learning — The Intuition of Hoeffding’s Inequality' :'https://najamogeltoft.medium.com/machine-learning-the-intuition-of-hoeffdings-inequality-970a59c2b519'}
    new_user_24 = {'24-51 things that can go wrong in a real-world ML project' :'https://medium.com/wrong-ml/51-things-that-can-go-wrong-in-a-real-world-ml-project-c36678065a75'}
    new_user_25 = {'25-Using Machine Learning to Classify Server Incidents' :'https://caiopedroso-data-ai.medium.com/using-machine-learning-to-classify-server-incidents-36f837c107a'}
    new_user_26 = {'26-Clean Architecture for AI/ML Applications using Dash and Plotly with Docker' :'https://towardsdatascience.com/clean-architecture-for-ai-ml-applications-using-dash-and-plotly-with-docker-42a3eeba6233'}
    new_user_27 = {'27-Measuring Success of Machine Learning Products' :'https://medium.com/codex/failure-is-part-of-the-learning-process-7f84cb26077b'}
    new_user_28 = {'28-Edit Your Old Photos with Machine Learning — Computational Photography' :'https://towardsdatascience.com/edit-your-old-photos-with-machine-learning-computational-photography-7ef27f40cfdf'}
    new_user_29 = {'29-Level-Up your Machine Learning Workflow with a Thunderbolt 3 SSD' :'https://towardsdatascience.com/level-up-your-machine-learning-workflow-with-a-thunderbolt-3-ssd-5682bcce8773'}
    new_user_30 = {'30-Machine learning model deployment with fast ai' :'https://medium.com/analytics-vidhya/machine-learning-model-deployment-with-fast-ai-658cfde878d0'}
    new_user_31 = {'31-MLOps: Model Monitoring 101' :'https://towardsdatascience.com/mlops-model-monitoring-101-46de6a578e03'}
    new_user_32 = {'32-Machine Learning With CameraX and MLKit' :'https://medium.com/swlh/machine-learning-with-camerax-and-mlkit-fbed9dcd542b'}
    new_user_33 = {'33-Explainable Machine Learning' :'https://towardsdatascience.com/explainable-machine-learning-9d1ca0547ae0'}
    new_user_34 = {'34-Why You Should Use Google Colab for Machine Learning Projects' :'https://medium.com/towards-artificial-intelligence/why-you-should-use-google-colab-for-machine-learning-projects-1d15d747b692'}
    new_user_35 = {'35-Serving Machine Learning Models (DCGAN, PGAN, ResNext) using FastAPI and Streamlit' :'https://medium.com/analytics-vidhya/serving-machine-learning-models-dcgan-pgan-resnext-using-fastapi-and-streamlit-2ef426f2e9de'}
    new_user_36 = {'36-Basics of Machine Learning: K-Means Clustering' :'https://medium.com/swlh/basics-of-machine-learning-k-means-clustering-f5c16678aa4'}
    new_user_37 = {'37-10 Tips to Learn Machine Learning Effectively' :'https://medium.com/swlh/10-tips-to-learn-machine-learning-72b7dcf15528'}
    new_user_38 = {'38-Meet Machine Learning, and its family!' :'https://medium.com/analytics-vidhya/meet-machine-learning-and-its-family-a86a85fb312c'}
    new_user_39 = {'39-Converting Machine Learning Models to SAS using m2cgen (Python)' :'https://towardsdatascience.com/converting-machine-learning-models-to-sas-using-m2cgen-python-190d846090dc'}
    new_user_40 = {'40-Introduction to the World of Machine Learning' :'https://medium.com/analytics-vidhya/introduction-to-the-world-of-machine-learning-94c2b265a878'}
    new_user_41 = {'41-The quickest way to build Dashboards for Machine Learning models' :'https://towardsdatascience.com/the-quickest-way-to-build-dashboards-for-machine-learning-models-ec769825070d'}
    new_user_42 = {'42-Geometric ML becomes real in fundamental sciences' :'https://towardsdatascience.com/geometric-ml-becomes-real-in-fundamental-sciences-3b0d109883b5'}
    new_user_43 = {'43-Machine Learning in compiler optimization' :'https://deep-patel18.medium.com/machine-learning-in-compiler-optimization-543d471ee22b'}
    new_user_44 = {'44-How to Present Machine Learning Results to Non-Technical People' :'https://towardsdatascience.com/how-to-present-machine-learning-results-to-non-technical-people-e096cc1b9f76'}
    new_user_45 = {'45-LIME: explain Machine Learning predictions' :'https://towardsdatascience.com/lime-explain-machine-learning-predictions-af8f18189bfe'}
    new_user_46 = {'46-Puzlee: The Kubernetes Cloud for Machine Learning Applications' :'https://towardsdatascience.com/puzl-ee-the-kubernetes-cloud-for-machine-learning-applications-770a07f70a2c'}
    new_user_47 = {'47-Auto-Sklearn: An AutoML tool based on Bayesian Optimization' :'https://towardsdatascience.com/auto-sklearn-an-automl-tool-based-on-bayesian-optimization-91a8e1b26c22'}
    new_user_48 = {'48-XAI — Build your own deep-learning interpretation algorithm' :'https://towardsdatascience.com/xai-build-your-own-deep-learning-interpretation-algorithm-6e471b59af7'}
    new_user_49 = {'49-Evaluating Semantic and Instance Segmentations' :'https://zpx01.medium.com/evaluating-semantic-and-instance-segmentations-874530713953'}
    new_user_50 = {'50-A Beginner’s Guide for Getting Started with Machine Learning' :'https://medium.com/analytics-vidhya/a-beginners-guide-for-getting-started-with-machine-learning-7ba2cd5796ae'}
    new_user_51 = {'51-Machine Learning: Unsupervised Learning' :'https://towardsdatascience.com/machine-learning-unsupervised-learning-928852ebaaeb'}
    new_user_52 = {'52-5 Essential Machine Learning Techniques for Business Applications' :'https://medium.com/swlh/5-essential-machine-learning-techniques-for-business-applications-f03f85cee2ba'}
    new_user_53 = {'53-Machine learning that pays the bills: choosing models in business contexts' :'https://towardsdatascience.com/machine-learning-that-pays-the-bills-choosing-models-in-business-contexts-e9003fd434a1'}
    new_user_54 = {'54-Optimising Particle Accelerators with Adaptive Machine Learning' :'https://medium.com/@researchoutreach/optimising-particle-accelerators-with-adaptive-machine-learning-8cce92626842'}
    new_user_55 = {'55-Experiment tracking in machine learning' :'https://towardsdatascience.com/experiment-tracking-in-machine-learning-ca4e4574941e'}
    new_user_56 = {'56-Cheat Sheets for Machine Learning Interview Topics' :'https://medium.com/swlh/cheat-sheets-for-machine-learning-interview-topics-51c2bc2bab4f'}
    new_user_57 = {'57-8 AutoML Libraries to Automate Machine Learning Pipeline' :'https://medium.com/swlh/8-automl-libraries-to-automate-machine-learning-pipeline-3da0af08f636'}
    new_user_58 = {'58-A brief introduction to Machine Learning' :'https://g1en19.medium.com/a-brief-introduction-to-machine-learning-b17b27e9aafb'}
    new_user_59 = {'59-Machine Learning with R: A Complete Guide to Linear Regression' :'https://towardsdatascience.com/machine-learning-with-r-a-complete-guide-to-linear-regression-6fad412f778'}
    new_user_60 = {'60-Using Machine Learning to Detect Bowel Cancer: Nathan Wan' :'https://towardsdatascience.com/using-machine-learning-to-detect-bowel-cancer-nathan-wan-24e67bedc0c1'}
    new_user_61 = {'61-Exploring Fundamental Machine Learning Concepts' :'https://medium.com/ai-in-plain-english/explaining-a-few-machine-learning-concepts-be3675c0c2f8'}
    new_user_62 = {'62-How to Start Your Machine Learning Career' :'https://medium.com/swlh/how-to-start-a-machine-learning-career-7b8d3cc36b3e'}
    new_user_63 = {'63-Interpretable Machine Learning — A Short Survey' :'https://maulik-parmar.medium.com/interpretable-machine-learning-a-short-survey-bb7b5ace7ae6'}
    new_user_64 = {'64-Introduction to the World of Machine Learning' :'https://medium.com/analytics-vidhya/introduction-to-the-world-of-machine-learning-94c2b265a878'}
    new_user_65 = {'65-Differential Equations Versus Machine Learning' :'https://medium.com/swlh/differential-equations-versus-machine-learning-78c3c0615055'}
    new_user_66 = {'66-Machine Learning in Production' :'https://towardsdatascience.com/machine-learning-in-production-95e1999bba84'}
    new_user_67 = {'67-The Rise of Machine Learning' :'https://towardsdatascience.com/the-rise-of-machine-learning-83f122e0aa34'}
    new_user_68 = {'68-Machine Learning System Design: Lessons from Facebook' :'https://medium.com/swlh/machine-learning-system-design-lessons-from-facebook-e78dc4db5372'}
    new_user_69 = {'69-How Quantum Computing May Benefit Machine Learning' :'https://towardsdatascience.com/how-may-quantum-computing-benefit-machine-learning-c96de0bef0d4'}
    new_user_70 = {'70-Credit Card Approval System using Machine Learning' :'https://abhinavsaurabh.medium.com/credit-card-approval-system-using-machine-learning-cb27615b23ef'}
    new_user_71 = {'71-Building machine learning intuition through play' :'https://towardsdatascience.com/building-machine-learning-intuition-through-play-2065fe487d46'}
    new_user_72 = {'72-Linear Algebra for ML' :'https://medium.com/towards-artificial-intelligence/linear-algebra-for-ml-61c9d1fed99d'}
    new_user_73 = {'73-How to Get Started with Machine Learning and AI' :'https://towardsdatascience.com/how-to-get-started-with-machine-learning-and-ai-16c082e406ee'}
    new_user_74 = {'74-CRISP-DM ready for Machine Learning Projects' :'https://towardsdatascience.com/crisp-dm-ready-for-machine-learning-projects-2aad9172056a'}
    new_user_75 = {'75-Completing the Machine Learning Loop' :'https://jimmymwhitaker.medium.com/completing-the-machine-learning-loop-e03c784eaab4'}
    new_user_76 = {'76-The Lesser of Two Evils in Machine Learning: Variance and Bias' :'https://examsherpa.medium.com/the-lesser-of-two-evils-in-machine-learning-variance-and-bias-d500f875efdb'}
    new_user_77 = {'77-Spatial Distance and Machine Learning' :'https://towardsdatascience.com/spatial-distance-and-machine-learning-2cab72fc6284'}
    new_user_78 = {'78-Unsupervised Machine Learning to Improve Data Quality' :'https://medium.com/build-something-cool/unsupervised-machine-learning-to-improve-data-quality-64edbffa684a'}
    new_user_79 = {'79-What is Ensemble Machine Learning? — using stories and pictures' :'https://abhinav-iitkgp2.medium.com/what-is-ensemble-machine-learning-using-stories-and-pictures-d949e4649a0f'}
    new_user_80 = {'80-Top Model Evaluation Metrics in Machine Learning' :'https://medium.com/datadriveninvestor/top-model-evaluation-metrics-in-machine-learning-51fcc11d7b7d'}
    new_user_81 = {'81-Solve problems with machine learning — what is machine learning anyway?' :'https://medium.com/analytics-vidhya/solve-problems-with-machine-learning-what-is-machine-learning-anyway-bb2d5339a88'}
    new_user_82 = {'82-Machine Learning with Microsoft’s Azure ML — Credit Classification' :'https://blog.clairvoyantsoft.com/machine-learning-with-microsofts-azure-ml-credit-classification-b928c29eb522'}
    new_user_83 = {'83-IPL Match Prediction based on Powerplay using Machine Learning' :'https://medium.com/ai-in-plain-english/ipl-match-prediction-based-on-powerplay-using-machine-learning-3b88c7ebce06'}
    new_user_84 = {'84-15 Greatest AI/ML Research Papers Of All Time' :'https://medium.com/datadriveninvestor/15-greatest-ai-ml-research-papers-of-all-time-401221761d1c'}
    new_user_85 = {'85-Automate your ML model retraining with Kubeflow' :'https://towardsdatascience.com/automate-your-ml-model-retraining-with-kubeflow-316f35afe19f'}
    new_user_86 = {'86-Overfitting and Underfitting In Machine Learning Algorithms' :'https://towardsdatascience.com/overfitting-and-underfitting-in-machine-learning-algorithms-b42694432bd7'}
    new_user_87 = {'87-Machine Learning in production: Keras, Flask, Docker and Heroku' :'https://towardsdatascience.com/machine-learning-in-production-keras-flask-docker-and-heroku-933b5f885459'}
    new_user_88 = {'88-A Machine Learning Approach to Estimating Reference Evapotranspiration' :'https://towardsdatascience.com/a-machine-learning-approach-to-estimating-reference-evapotranspiration-2adf58d2eb91'}
    new_user_89 = {'89-Machine Learning Intern Journal — Federated Learning' :'https://medium.com/impactia/machine-learning-intern-journal-federated-learning-c7df02ce5914'}
    new_user_90 = {'90-Fixing the Conflict Between Math and Machine Learning' :'https://medium.com/swlh/fixing-the-conflict-between-math-and-machine-learning-80c4f8cc760e'}
    new_user_91 = {'91-Apple’s M1 is Up to 3-6x as Fast at Training Machine Learning Models' :'https://medium.com/swlh/apples-m1-is-up-to-as-3-6x-fast-at-training-machine-learning-models-2b1df47c3da6'}
    new_user_92 = {'92-Linear Regression (Getting Started With Machine Learning)' :'https://medium.com/carre4/linear-regression-getting-started-with-machine-learning-c2dae103ad16'}
    new_user_93 = {'93-Building a Machine Learning Pipeline with Scikit-Learn' :'https://towardsdatascience.com/building-a-machine-learning-pipeline-3bba20c2352b'}
    new_user_94 = {'94-Deploy your Machine Learning Model with ml5 js' :'https://towardsdatascience.com/deploy-your-machine-learning-model-with-ml5-js-5202aaa48dbf'}
    new_user_95 = {'95-Explaining Machine Learning to Grandma: Tree-based Models' :'https://medium.com/ai-in-plain-english/explaining-machine-learning-to-grandma-tree-based-models-62fbc50e0bb6'}
    new_user_96 = {'96-Busting AI Myths: “Machine Learning is Expensive”' :'https://medium.com/datadriveninvestor/busting-ai-myths-machine-learning-is-expensive-7005c0e01c21'}
    new_user_97 = {'97-Machine Learning in Baseball' :'https://towardsdatascience.com/machine-learning-in-baseball-bbe91af05db7'}
    new_user_98 = {'98-How to make bar and hbar charts with labels using matplotlib' :'https://towardsdatascience.com/how-to-make-bar-and-hbar-charts-with-labels-using-matplotlib-b701ce70ba9c'}
    new_user_99 = {'99-How to train a Bayesian Network (BN) using expert knowledge?' :'https://towardsdatascience.com/how-to-train-a-bayesian-network-bn-using-expert-knowledge-583135d872d7'}
    new_user_100 = {'100-Classifiers in Machine Learning' :'https://medium.com/btechmag/classifiers-in-machine-learning-c7d17d1f38b'}

    new_users = [new_user_1, new_user_2, new_user_3,new_user_4,new_user_5,new_user_6,new_user_7,new_user_8,new_user_9,new_user_10,new_user_11,new_user_12,new_user_13,new_user_14,new_user_15,new_user_16,new_user_17,
    new_user_18,new_user_19,new_user_20,new_user_21,new_user_22,new_user_23,new_user_24,new_user_25,new_user_26,new_user_27,new_user_28,new_user_29,new_user_30,new_user_31,new_user_32,new_user_33,new_user_34,new_user_35,
    new_user_36,new_user_37,new_user_38,new_user_39,new_user_40,new_user_41,new_user_42,new_user_43,new_user_44,new_user_45,new_user_46,new_user_47,new_user_48,new_user_49,new_user_50,new_user_51,new_user_52,new_user_53,
    new_user_54,new_user_55,new_user_56,new_user_57,new_user_58,new_user_59,new_user_60,new_user_61,new_user_62,new_user_63,new_user_64,new_user_65,new_user_66,new_user_67,new_user_68,new_user_69,new_user_70,new_user_71,
    new_user_72,new_user_73,new_user_74,new_user_75,new_user_76,new_user_77,new_user_78,new_user_79,new_user_80,new_user_81,new_user_82,new_user_83,new_user_84,new_user_85,new_user_86,new_user_87,new_user_88,new_user_89,
    new_user_90,new_user_91,new_user_92,new_user_93,new_user_94,new_user_95,new_user_96,new_user_97,new_user_98,new_user_99,new_user_100]
    db_enter.insert_many(new_users)
    result = {'result' : 'Created successfully'}
    return result

if __name__ == '__main__':
    app.run(debug=True)