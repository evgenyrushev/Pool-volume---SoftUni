pool_volume = int(input())
pipe_one_debit = int(input())
pipe_two_debit = int(input())
hours_absent = float(input())

filled_pool = pipe_one_debit * hours_absent + pipe_two_debit * hours_absent
percentage_volume_filled = (filled_pool / pool_volume) * 100
pipe_one_percentage = ((pipe_one_debit * hours_absent) / filled_pool) * 100
pipe_two_percentage = ((pipe_two_debit * hours_absent) / filled_pool) * 100

if filled_pool <= pool_volume:
    print(f"The pool is {percentage_volume_filled:.2f}% full. Pipe 1: {pipe_one_percentage:.2f}%. "
      f"Pipe 2: {pipe_two_percentage:.2f}%.")
else:
    print(f"For {hours_absent:.2f} hours the pool overflows with {filled_pool - pool_volume:.2f} liters.")
