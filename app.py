#!/usr/bin/env python3

from aws_cdk import core

from lambda_reg_counter.lambda_reg_counter_stack import LambdaRegCounterStack


app = core.App()
LambdaRegCounterStack(app, "lambda-reg-counter")

app.synth()
