# Empirical Method Signals

Use these signals after the general method review. They prompt targeted inspection and do not replace design-specific expertise. Never turn one conventional threshold into an automatic verdict.

## Design and data generation

- Reconstruct how observations entered the sample and whether inclusion depends on treatment, exposure, outcome, disclosure, survival, or data availability.
- Check the unit of analysis, repeated observations, clustering, nesting, spatial dependence, and temporal dependence.
- Check whether the observation window captures anticipation, adjustment, lagged effects, and structural breaks.
- Examine missingness, attrition, outliers, winsorization, imputation, and sample exclusions.
- Check whether the sample represents the population to which conclusions are generalized.

## Measurement and constructs

- Check content validity, convergent validity, discriminant validity, reliability, and measurement invariance when relevant.
- Inspect item wording and source overlap when respondents may not distinguish constructs.
- Treat HTMT, factor loadings, alpha, composite reliability, AVE, VIF, and similar metrics as evidence interpreted in context, not pass or fail switches.
- Investigate common-method risk through design, timing, source separation, markers, latent methods, or other suitable approaches. Do not rely on one post hoc test alone.
- Check whether text-derived, rating-derived, or disclosure-derived measures overlap mechanically with outcomes, mediators, or mechanisms.
- Check whether a proxy captures the construct across industries and time.

## Statistical specification

- Check functional form, interactions, nonlinear terms, fixed effects, random effects, controls, trends, and error structure.
- Require a theoretical or design reason for controls and avoid bad controls affected by treatment.
- Check multicollinearity when coefficients are unstable, signs are implausible, or constructs overlap.
- Check multiplicity, researcher degrees of freedom, specification search, and selective reporting.
- Report effect magnitudes and uncertainty in addition to p-values.
- For nonlinear claims, test and visualize the relationship over the observed support. Do not infer a global curve from significance in one subgroup or quantile.

## Causal and quasi-experimental designs

- Identify the treatment, timing, assignment mechanism, comparison group, estimand, and identifying assumption.
- For difference-in-differences, inspect pretrends, anticipation, staggered timing, treatment heterogeneity, contamination, and estimator suitability.
- For instruments, inspect relevance, exclusion, monotonicity, interpretation, and weak-instrument risk.
- For regression discontinuity, inspect manipulation, bandwidth, functional form, local balance, and local scope.
- For matching or weighting, inspect overlap, balance, model dependence, and post-treatment variables.
- For natural experiments, require a credible institutional account of why the shock is plausibly exogenous.
- Robustness must target the central identification threat with placebo, falsification, alternative timing, alternative outcome, negative control, or sensitivity analysis as appropriate.

## Survey and SEM studies

- Check the target population, recruitment, response rate, nonresponse, informant competence, and minimum information size.
- Check whether the measurement model supports distinctions used in the structural model.
- Inspect collinearity, discriminant validity, endogeneity, fit or predictive metrics, mediation timing, and moderation support as appropriate to covariance or partial-least-squares SEM.
- Check whether cross-sectional self-reports are used to claim temporal mediation or causality.
- Require questionnaire items, scales, translation procedures, pilot testing, and adaptation rationale.

## Panel, time-series, and quantile studies

- Check stationarity, cointegration, cross-sectional dependence, serial correlation, lag selection, breaks, and dynamic bias as relevant.
- Check whether fixed effects absorb the variation required for the focal estimate.
- For quantile methods, keep interpretations quantile-specific and test whether cross-quantile differences are meaningful.
- Check whether country or aggregate panels have enough independent information for the model complexity.
- Examine major shocks and report sensitivity to their inclusion.

## Text as data, LLM, and machine-coded variables

- Report corpus construction, document selection, parsing, language handling, model and version, prompts, decoding, preprocessing, and aggregation.
- Validate labels against a transparent human-coded or otherwise credible benchmark.
- Report accuracy and class-specific performance with uncertainty when feasible.
- Check temporal leakage, outcome leakage, training-data contamination, and use of information unavailable at the claimed decision time.
- Check reproducibility when remote models change over time.
- Examine whether the constructed variable duplicates information in an outcome, mediator, or disclosure measure.
- Check industry and language heterogeneity and perform error analysis rather than reporting one average metric.

## Robustness and heterogeneity

- Prioritize alternative operationalizations and analyses that address the main threat.
- Require heterogeneity to follow theory, institutional logic, or a prespecified question.
- Treat multiple subgroup results cautiously when power and multiplicity are not addressed.
- Check whether conclusions survive economically plausible effect sizes and alternative samples.
- Distinguish robustness of sign, magnitude, inference, mechanism, and practical conclusion.
