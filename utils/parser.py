import re
 
class Parser:
	def __init__(self, domain, plan):
		self.domain = domain
		self.plan = plan
		self.action_params = {}
		self.preconditions = {}
		self.postconditions = {}
		self.regex_outer_parentheses = "\((\(*(?:[^)(]*|\([^)]*\))*\)*)\)" # reference: https://stackoverflow.com/questions/56519862/remove-outermost-parentheses

	def parse_domain_action(self):
		action = self.line.split("(:action ", 1)[1].strip()
		return action

	def parse_plan(self):
		output = ""
		stack_pre = []
		stack_params = []
		with open(self.plan) as plan_file:
			for line in plan_file:
				self.line = line
				breakpoint()
				if self.line.starstwith("("):
					action, param_values = self.parse_plan_action()
					for pre, param in zip(preconditions, param_values):
						output += f"if {pre}({param}):\n"
						stack_pre.append(pre)
						stack_params.append(param)
					output_line = f"{action}("
					for param, param_value in zip(self.action_params[action], param_values):
						output_line += f"{param}={param_value}, "
					output += f"{output_line[:-2]})"
					while stack:
						output += f"else:\n\traise AssertionError('Precondition error. {stack_pre.pop()} is not {stack_params.pop()}')"
					for post, param in zip(postconditions, param_values):
						output += f"if not {post}({param}):\n\traise AssertionError('Precondition error. {post} is not {param}')"

	def parse_plan_action(self):
		plan_action_elements = re.search(self.regex_outer_parentheses, self.line).group(1).split()
		action, param_values = plan_action_elements[0], plan_action_elements[1:]
		return action, param_values

	def parse_domain(self):
		in_pre = False
		in_post = False
		with open(self.domain) as domain_file:
			for line in domain_file:
				self.line = line.strip()
				if in_pre:
					if self.line.startswith(")"):
						in_pre = False
					else:
						self.preconditions[action].append(self.parse_predicate(self.line, param_dict))
				if in_post:
					if self.line.startswith(")"):
						in_post = False
					else:
						self.postconditions[action].append(self.parse_predicate(self.line, param_dict))
				if self.line.startswith("(:action"):
					action = self.parse_domain_action()
				elif self.line.startswith(":parameters"):
					param_dict = self.parse_domain_params(action)
				elif self.line.startswith(":precondition"):
					in_pre = True
					self.preconditions[action] = []
					curr_line_pred = self.line.split(":precondition (", 1)[1]
					if not curr_line_pred.startswith("and"):
						self.preconditions[action].append(self.parse_predicate(curr_line_pred, param_dict))
				elif self.line.startswith(":effect"):
					in_post = True
					self.postconditions[action] = []
					curr_line_pred = self.line.split(":effect ", 1)[1]
					if not curr_line_pred.startswith("(and"):
						self.postconditions[action].append(self.parse_predicate(curr_line_pred, param_dict))

	def parse_domain_params(self, action):
		param_tuples = re.findall("(\?\w+)\s-\s(\w+)", self.line)
		param_dict = {}
		self.action_params[action] = []
		for param_tuple in param_tuples:
			param_dict[param_tuple[0]] = param_tuple[1] # format --> key: "?x" value: "description(x)"
			self.action_params[action].append(param_tuple[1]) # returning a list of lifted parameters
		return param_dict

	def parse_predicate(self, line, param_dict):
		line = re.search(self.regex_outer_parentheses, line).group(1)
		if line.startswith("not"):
			pred_list = re.search(self.regex_outer_parentheses, line).group(1).split()
			pred_list[0] = f"not({pred_list[0]})"
		else:
			pred_list = line.split()
		pred_results = self.parse_pred_vals(pred_list, param_dict)
		return pred_results

	def parse_pred_vals(self, pred_list, param_dict):
		pred_names = []
		for i, element in enumerate(pred_list):
			if i == 0:
				pred = element
			else:
				pred_names.append(param_dict[element])
		return [pred, pred_names]

if __name__ == "__main__":
	parser = Parser("sandwich/domain.pddl", "sandwich/make_sandwich.pddl")
	parser.parse_domain()
	parser.parse_plan()