## Rebuttal

Many thanks for the great comments! Please find our replies below.



某个大实验是不是可以做：

This is an exciting experiment that we have not investigated! We began with ... in order to start from a near SOTA trunk model. It may be that ... We will try this and report results in the camera ready as we cannot report it here.

# ECCV

factual error, refrain from requesting significant experiments

We sincerely thank the reviewers for their positive comments like technically sound and reasonble (R1), innovative (R2), and insightful suggestions that are helpful to the community (R3). Our response to all comments can be found below.

## R1: 

1. Guideline for hyperparameter tuning

   $\lambda_p$ and $\lambda_n$: The concrete forms of $\lambda_p$ and $\lambda_n$ depend on how to reweight each pair and debias the negative sampling (Section 3.2), rather than directly setting. We reweight negative pair by similarity to emphasize hard negative and resort to PU-learning to debias, while how to reweight positive samples is a problem to explore.

   Similarity functions should be asymmetric. Beyond various tunable asymmetric functions that designed and tuned by hand, we think the most interesting thing is to design a learnable asymmetric function and convert the tuning to a learnable process.

   $\alpha$ should be non-increasing w.r.t. $d$. In our experiments, we find simple linear schedule performs well, readers can also try other monotonically decreasing functions, while we assume this may not be of much importance.

   $\gamma$: similar to TRADES, this is a parameter balancing the trade-off between natural and robutst accuracy, i.e., as $\gamma$ Increases, natural accuracy decreases while robust accuracy increases until a peak.

   $\tau$: can refer to HCL and DCL and use as they suggest

2. why the proposed method has not been introduced into standard contrastive learning:

   It's really a great question, and we also considered it when we were working on this paper. We have a short discussion in the last paragraph of Section 2. We believe there exists asymmetry between various strong augmentations used in CL. To utilize this method in CL, we think it's critical to have deeper understanding about the used strong augmentations, to make clear whether they have relative good or bad in 'quality'. Such things are not clear now and making clear view A is 'better' than view B is quite difficult, moreover, how to define the 'better/quality' also depends, we think these are two possible reasons for the question, while adversary is the clearest guy that are worst, misleading the model and shouldn't attract clean views.

## R2:

1. Experiments results are less: 

   1. for standard CL method, it is a large problem worth exploring, as stated in R1Q2.
   2. for adversarial CL method, using CL to enhance robustness has emerged just recently, there only exists three methods typically, RoCL, ACL and AdvCL. ACL used a two-stream architecture and doesn't use contrast between adversarial view and clean view, which is another line of adversarial contrastive learning and not typical. While the state-of-the-art method (AdvCL) used contrast between adversarial and clean views, we apply our method to it and the first method (RoCL), to show the effectiveness of our method.

   To enrich the experiments, we will add more evaluation on robustness under diverse attacks to show effectiveness. Moreover, because it can be used readily.

2. Some errors: 

   We thank the reviewer for pointing out the statement issue and sorry for the puzzlement brought by our wrong statement. We have fixed it and checked through the article to avoid puzzles or typos like this for ease of understanding. Thanks!

## R3:

### Other attacks:

We first present experiment results under one-pixel attack, spatial transformation attack and color channel attack mentioned by R3. Moreover, to enrich the kinds of attacks as suggested by R3, we also test the robustness under AutoAttack (consists of an emsemble of four strong diverse attacks and is widely considered as the strongest attack used for robustness evaluation now), CW attack, and strong PGD attack. Experiments results show that our methods can improve robustness under all ...

We respectfully disagree with R3 that we didn't focus "our method improves robustness in multi-faceted manner", we actually focus on (unlabeled) adversarial training for improving worst-case "adversarial robustness", which is commonly evaluated under PGD-class attacks, e.g., all works reviewed in "Section 5. *Adversarial Training*". 

The main body research in adversarial training use PGD and its variations for robustness evaluation, because PGD is widely considered as the universally strongest first-order attack [1]. For evaluation, we naturally follow the common practice and the main body literature on adversarial robustness, and all close-related articles on adversarial CL [] are evaluated in this way. But we sincerely agree with R3's insightful suggestions that some other vulnerablity of DL may not be improved under such evaluation, and are willing to provide results under diverse attacks and will append the full results to the appendix.

### Dataset & hardward setup.

We agree with R3's point that results for small datasets may not be scaled to large-scale datasets. while it's really hard and expensive to perform adversarial training on ImageNet. Adversarial training is usually 10 times slower than natural training, cause the generation of adversarial examples needs multiple gradient steps, making it really hard to evaluate adversarial training methods on large-scale datasets like ImageNet. By a rough statistics, only 4 of 18 papers on adversarial training in ICLR 2022 evaluate their methods on full ImageNet, with several others use a subset of ImageNet with 10 or 100 classes. Given the huge resource demands that are not affordable by most of the community, we think lack of results on ImageNet can hardly become a reason for directly rejecting a paper in the area of adversarial training.

About hardware setup, we use 4 V100 GPUs to finish all experiments in our paper.

Outlier: prevent these outliers attracting our clean representations
Instance-level identity, not class-level. Contrastive learning has objective to discriminate each instance, while may push, which is contradicted to CL's objective.

Note that adversarial examples generated in unlabeled contrastive learning have intrinsic property to reside far away from the current instance and head towards other instances. (Because contrastive loss aims at pulling close positive pairs, and pushing away negatives, the generation of adversaries is definitely a reverse process.) Our evaluation are nearly the same with the previous works, while we are willing to provide results under various attacks.

Adversarial Attack chosen for evaluation:

1、补实验；2、说明道理

尽管他们强

这些探索是有必要的，但是我们的文章确实是针对于adversarial robustness

我们的article的立足点确实是adversarial robustness against the PGD-class optimization-based "strongest attacks" like various related works. 

"Adversarial robustness" 通常指的是针对FGSM, BIM, PGD, CW, AA等optimization-based strong attack on the overall image (all pixels of image)，one pixel attack is not strong. The community rarely use them to evaluate model's robustness. 

Adversarial training on large-scale datasets really costs a lot that we are not affordable, cause adversarial training traditionally cost 几倍 compared to natural training.  Moreover, our adversarial contrastive learning scheme is pre-training then finetuning, which can be seen as having an extra pretraining stage than adversarial training, even cost more. 



SELF-ENSEMBLE ADVERSARIAL TRAINING FOR IMPROVED ROBUSTNESS. CIFAR-10/-100
EXPLORING MEMORIZATION IN ADVERSARIAL TRAINING. CIFAR-10/-100/SVHN. PGD CW AA
IMPLICIT BIAS OF ADVERARIAL TRAINING FOR DEEP NEURAL NETWORKS. MNIST. FGSM, PGD
Improved deterministic l2 robustness on CIFAR-10 and CIFAR-100. 
ROBUST UNLEARNABLE EXAMPLES: PROTECTING DATA AGAINST ADVERSARIAL LEARNING. CIFAR-10/-100/IMN(100 class)
A UNIFIED CONTRASTIVE ENERGY-BASED MODEL FOR UNDERSTANDING THE GENERATIVE ABILITY OF ADVERSARIAL TRAINING. CIFAR-10
Concurrent Adversarial Learning for Large-Batch Training. IMAGENET
Robust Learning Meets Generative Models: Can Proxy Distributions Improve Adversarial Robustness? ImageNet
RELIABLE ADVERSARIAL DISTILLATION WITH UNRELIABLE TEACHERS
3 / 15 (focus on large batch training)
1 re-scaled to 128x128 by DeepMind
1 tiny imagenet
1 10class
1 100 class

## AC

1. In adversarial training, lack of results ImageNet has never become a reason for directly rejecting, meanwhile regardless of the intuitive motivation, innovative idea, reasonable method and clear writing as commented by other reviewers. 
   Due to the huge resources demanded for adversarial training, the common practice in the community is evaluating methods on MNIST, CIFAR-10, CIFAR-100.
2. For evaluation, color channel attack is only cited by 5. It's not a commonly used attack in the community for evaluation. PGD attack is generally the strongest attack and we carefully follow the communities' practice to use such attacks for evaluation. We are willing to evaluate on various attacks but we think it should not be a firm reason for strong reject that we didn't evaluate under such attack in the original version.

CIFAR-10/-100. We think lack for reject. We don't think this is the 'main weakness'

