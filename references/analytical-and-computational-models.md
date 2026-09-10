# Analytical and Computational Models

Use this reference for mathematical models, optimization, game theory, Markov processes, simulation, machine learning, and related computational research. Apply the general method reference first.

## Contents

- Model purpose and contribution
- Entities, timing, and information
- Assumptions and micro-foundations
- Derivation and solution quality
- Game theory
- Evolutionary games
- Markov and stochastic models
- Optimization and operations models
- Simulation
- Machine learning and AI models
- Numerical analysis and sensitivity
- Interpretation and implications

## Model purpose and contribution

- State whether the model explains a mechanism, predicts outcomes, optimizes a decision, compares institutions, or explores scenarios.
- Check whether the model structure is necessary for the research question.
- Compare the focal mechanism with simpler service, quality, information, trust, spillover, or cost mechanisms.
- Check whether the main result is nontrivial or is directly encoded in payoffs, utility, constraints, or ordering assumptions.
- Apply the substitution test to the focal technology and context.

## Entities, timing, and information

- Identify actors, objectives, decisions, constraints, information sets, and outside options.
- Check whether the sequence of decisions matches the real adjustment speed and institutional process.
- Check commitment, observability, rationality, foresight, and information assumptions.
- Examine whether actors can distinguish alternatives in the way assumed by demand or utility.
- Check whether an omitted actor or transfer carries the cost or benefit that drives the result.

## Assumptions and micro-foundations

- Require theoretical, empirical, institutional, or case support for consequential assumptions.
- Distinguish normalization for tractability from an economically meaningful restriction.
- Check support, distribution, parameter range, cost incidence, and functional form.
- Require a behavioral or institutional account for trust, privacy, fairness, preference, spillover, learning, or adoption terms.
- Examine whether binary consumer types erase heterogeneity central to the research question.
- Test plausible alternative assumptions rather than only restating the baseline.

## Derivation and solution quality

- Check objective functions, constraints, first-order and second-order conditions, corner solutions, and feasibility.
- Require equilibrium existence, uniqueness, stability, and parameter conditions when relevant.
- Check whether thresholds stay within their stated domain.
- Check that propositions identify the conditions under which results hold.
- Require derivations or appendices sufficient for independent verification.
- Distinguish analytical proof from numerical illustration.

## Game theory

- Check player order, strategic variables, equilibrium concept, beliefs, commitment, and outside options.
- Compare centralized, decentralized, cooperative, and contractual cases only when objectives and transfers are consistently specified.
- For coordination claims, verify participation constraints, budget balance, implementability, and distribution of gains.
- For repeated or dynamic games, check state dependence, updating, continuation values, and time consistency.
- Check whether comparative statics cover economically relevant regions rather than one interior solution.

## Evolutionary games

- Distinguish stationary points, interior equilibria, local stability, asymptotic stability, and evolutionarily stable strategies.
- Derive the dynamic system from explicit payoffs and population assumptions.
- Check boundary equilibria and the full feasible state space.
- Verify Jacobian, eigenvalue, or Lyapunov reasoning used for stability.
- Check whether the population interpretation and imitation or learning process fit the application.
- Do not label every stable numerical trajectory as an ESS.

## Markov and stochastic models

- Define states so that they are mutually meaningful and sufficiently informative.
- Justify the Markov property, transition mechanism, time step, and homogeneity or nonhomogeneity assumption.
- Check transition probabilities, absorbing states, ergodicity, recurrence, stationarity, and initial conditions as relevant.
- Explain how transition parameters are estimated, calibrated, or elicited.
- Test sensitivity to state definitions, transition uncertainty, horizon, and structural breaks.
- Validate predicted state occupancy, passage time, or long-run behavior against independent evidence when possible.

## Optimization and operations models

- Check objectives, constraints, decision variables, feasibility, units, and tradeoffs.
- Compare with credible baselines, heuristics, or current practice.
- Check convexity, duality, optimality guarantees, approximation quality, and computational complexity as applicable.
- Test scalability, instance generation, solver settings, time limits, optimality gaps, and randomness.
- Separate an optimal solution under assumptions from an implementable policy.

## Simulation

- Check model initialization, event logic, agents, distributions, calibration, warm-up, horizon, replications, and random seeds.
- Require verification of code logic and validation of model behavior.
- Report Monte Carlo uncertainty and convergence.
- Test alternative scenarios and assumptions over defensible ranges.
- Check whether the simulation is used to infer beyond the model that generated it.

## Machine learning and AI models

- Define task, target, inputs, split strategy, baseline, evaluation metric, and deployment context.
- Prevent train-test contamination, temporal leakage, group leakage, and tuning on the test set.
- Compare with strong simple baselines and ablations that isolate the proposed contribution.
- Check class imbalance, calibration, uncertainty, robustness, subgroup performance, and distribution shift.
- Report model version, preprocessing, hyperparameters, seeds, compute, and access constraints.
- Distinguish predictive gain from causal, theoretical, or managerial explanation.

## Numerical analysis and sensitivity

- Justify parameter values and ranges with cited data, cited literature, institutional facts, or documented real cases. Transparent normalization may establish scale, but it does not by itself establish empirical plausibility.
- Trace every calibrated or selected value to a source, estimation procedure, case observation, or clearly labeled illustrative assumption.
- Explain why cited evidence transfers to the modeled actor, market, period, and decision setting.
- Explore the full feasible and economically meaningful region.
- Check discontinuities, multiple optima or equilibria, sign reversals, and boundary cases.
- Use numerical figures to illustrate established properties, not to substitute for missing analytical conditions.
- Check whether extensions genuinely challenge the mechanism rather than reproduce the baseline result.

## Interpretation and implications

- Trace every managerial or policy implication to a modeled actor, decision, mechanism, and result.
- Do not recommend a contract, governance scheme, investment-sharing rule, or intervention that is absent from the model.
- State limitations caused by tractability assumptions, omitted dynamics, omitted actors, and calibration.
- Describe threshold results as conditional and avoid universal advice.
- In a Management Insights section, translate comparative statics or numerical patterns into feasible choices under identifiable information, resource, incentive, and institutional constraints.
