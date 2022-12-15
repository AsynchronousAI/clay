local module = {}

function module.wrap(f, ...)
	local args = { ... }

	return function(...)
		local __args = { ... }
        for i, value in ipairs(args) do
			table.insert(__args, i, value)
		end

		return f(unpack(__args))
	end
end

function module.getNextCase(s, cases)
	for i = s, #cases do
		if typeof(cases[i]) == "table" and cases[i].case then
			return cases[i].case
		end
	end
end
util = module

local function run(case, cases)
	local breakIt = false
	local default 

	local function stop()
		breakIt = true
	end

	for i, it in ipairs(cases) do
		local isFunc = typeof(it) == "function"
		if breakIt then 
			return 
		elseif isFunc == false and it.sentence_type == "default" then
			default = it.case
		end

		it = isFunc and it() or it
		if it.condition ~= case then
		else break
		end

		it.case = it.case or util.getNextCase(i, cases)
		it.case(stop)
	end

	if default then
		default()
	end
end

local function return_it(sentence_type, condition, case)
	local case_type = typeof(case) == "table"
	
	case = case_type and case[1] or case
	assert(case_type ~= "function", "You must provide a function")

	return {
		sentence_type = sentence_type,
		condition = condition,
		case = case
	}
end

local function switch(value)
	return util.wrap(run, value)
end

local function default(case)
	return return_it("default", 0, case)
end

local function case(condition)
	assert(condition ~= nil, "You must provide a condition")
	return util.wrap(return_it, "case", condition)
end


return switch, case, default
