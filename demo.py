Input:
    D = {(Xi, yi)}          # Original experimental dataset
    N_aug                   # Target augmented training size
    K = 100                 # Number of independent random splits
    alpha                   # Gaussian perturbation factor
    q                       # Mahalanobis distance quantile

Output:
    Performance metrics (Mean ± SD)

1. For k = 1 to K:

    # Split original data before augmentation
    Split D into D_train and D_test (80:20, stratified)

    # Estimate parameters from training data only
    Compute feature statistics and Mahalanobis threshold
    Train RF, SVC, and CatBoost on D_train

    Initialize D_aug = D_train

    # Generate synthetic training samples
    While |D_aug| < N_aug:

        Generate candidate X_new using Gaussian
        perturbation or adaptive interpolation

        Recalculate Ni/Si ratio

        # Apply physical and statistical constraints
        If physical constraints are violated:
            Continue

        If Mahalanobis distance exceeds threshold:
            Continue

        If X_new is duplicated:
            Continue

        # Ensemble-based label screening
        Predict labels using RF, SVC, and CatBoost

        If majority vote agrees with inherited label:
            Add (X_new, y_new) to D_aug

    # Final refinement of augmented data
    Apply outlier filtering and class balancing

    # Evaluate augmentation effectiveness
    Train M_original on D_train
    Train M_augmented on D_aug

    Evaluate both models on the same untouched D_test

    Record Accuracy, Precision, Recall, and F1-score

2. Calculate Mean ± SD across K independent splits

3. Report original and augmented model performance

4. Return evaluation results
