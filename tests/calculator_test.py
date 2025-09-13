# import sys
# from io import StringIO
# import contextlib
# from app.calculator import calculator  # adjust import if needed

# def run_calculator_with_input(monkeypatch, inputs):
#     """Simulate user input.
#     param monkeypatch: pytest fixture to simulate user input
#     param inputs: list of strings representing simulated input
#     return: captured output as a string
#     """

#     input_iter = iter(inputs)
#     monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

#     capture_output = StringIO()
#     with contextlib.redirect_stdout(capture_output):
#         calculator()

#     return capture_output.getvalue()
