from flask import Flask, request, render_template

app = Flask(__name__)

class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        num_set = set(nums)
        longest_sequence = 0

        for num in num_set:
            # Only check for the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_sequence = 1

                # Check the length of the sequence starting from current_num
                while current_num + 1 in num_set:
                    current_num += 1
                    current_sequence += 1

                longest_sequence = max(longest_sequence, current_sequence)

        return longest_sequence

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            nums = list(map(int, request.form['nums'].split(',')))
            solution = Solution()
            result = solution.longestConsecutive(nums)
        except ValueError:
            result = "Invalid input. Please enter a list of integers separated by commas."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)