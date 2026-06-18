# Project 04: Responsible AI Assistant Guardrails

## Purpose

This project demonstrates a responsible AI evaluation framework for a support assistant. It uses synthetic prompt test cases and sample responses to show how hallucination risk, unsupported claims, and unclear escalation needs can be flagged.

This is not connected to an LLM API. It is a public-safe framework that can later be extended to test real model outputs.

## Business problem

AI assistants can improve productivity, but they need governance. Ambiguous prompts, missing source material, and overconfident responses can create risk for employees and customers.

## Solution approach

1. Define prompt test cases.
2. Identify risk type and expected behavior.
3. Evaluate sample assistant responses for simple guardrail signals.
4. Create a pass/fail output with notes.
5. Maintain a risk register and governance checklist.

## Run the demo

```bash
python3 project_04_responsible_ai_assistant_guardrails/src/evaluate_guardrails.py
```

## Skills demonstrated

- Responsible AI thinking
- Prompt evaluation planning
- Risk register design
- Guardrail testing
- Explainability documentation
- Governance and monitoring mindset
