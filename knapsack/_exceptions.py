import gurobipy as gp

class GurobiError(gp.GurobiError):

    errno = -1
    argument = ""

    def __init__(self):
        super().__init__(self.errno, self.argument)


class GRBOutOfMemory(GurobiError):
    errno = 10001 
    argument = "Available memory was exhausted"


class GRBNullArgument(GurobiError):
    errno = 10002 
    argument = "NULL input value provided for a required argument"


class GRBInvalidArgument(GurobiError):
    errno = 10003 
    argument = "An invalid value was provided for a routine argument"


class GRBUnknownAttribute(GurobiError):
    errno = 10004 
    argument = "Tried to query or set an unknown attribute"


class GRBDataNotAvailable(GurobiError):
    errno = 10005 
    argument = "Attempted to query or set an attribute that could not be accessed at that time"


class GRBIndexOutOfRange(GurobiError):
    errno = 10006 
    argument = "Tried to query or set an attribute, but one or more of the provided indices (e.g., constraint index, variable index) was outside the range of valid values"


class GRBUnknownParameter(GurobiError):
    errno = 10007 
    argument = "Tried to query or set an unknown parameter"


class GRBValueOutOfRange(GurobiError):
    errno = 10008 
    argument = "Tried to set a parameter to a value that is outside the parameter's valid range"


class GRBNoLicense(GurobiError):
    errno = 10009 
    argument = "Failed to obtain a valid license"


class GRBSizeLimitExceeded(GurobiError):
    errno = 10010 
    argument = "Attempted to solve a model that is larger than the limit for a demo license"


class GRBCallback(GurobiError):
    errno = 10011 
    argument = "Problem in callback"


class GRBFileRead(GurobiError):
    errno = 10012 
    argument = "Failed to read the requested file"


class GRBFileWrite(GurobiError):
    errno = 10013 
    argument = "Failed to write the requested file"


class GRBNumeric(GurobiError):
    errno = 10014 
    argument = "Numerical error during requested operation"


class GRBIisNotInfeasible(GurobiError):
    errno = 10015 
    argument = "Attempted to perform infeasibility analysis on a feasible model"


class GRBNotForMip(GurobiError):
    errno = 10016 
    argument = "Requested operation not valid for a MIP model"


class GRBOptimizationInProgress(GurobiError):
    errno = 10017 
    argument = "Tried to query or modify a model while optimization was in progress"


class GRBDuplicates(GurobiError):
    errno = 10018 
    argument = "Constraint, variable, or SOS contained duplicated indices"


class GRBNodefile(GurobiError):
    errno = 10019 
    argument = "Error in reading or writing a node file during MIP optimization"


class GRBQNotPsd(GurobiError):
    errno = 10020 
    argument = "Q matrix in QP model is not positive semi-definite"


class GRBQcpEqualityConstraint(GurobiError):
    errno = 10021 
    argument = "QCP equality constraint specified (only inequalities are supported unless the NonConvex parameter is set to 2)"


class GRBNetwork(GurobiError):
    errno = 10022 
    argument = "Problem communicating with the Gurobi Compute Server"


class GRBJobRejected(GurobiError):
    errno = 10023 
    argument = "Gurobi Compute Server responded, but was unable to process the job (typically because the queuing time exceeded the user-specified timeout or because the queue has exceeded its maximum capacity)"


class GRBNotSupported(GurobiError):
    errno = 10024 
    argument = "Indicates that a Gurobi feature is not supported under your usage environment (for example, some advanced features are not supported in a Compute Server environment)"


class GRBExceed2bNonzeros(GurobiError):
    errno = 10025 
    argument = "Indicates that the user has called a query routine on a model with more than 2 billion non-zero entries, and the result would exceed the maximum size that can be returned by that query routine. The solution is typically to move to the GRBX version of that query routine."


class GRBInvalidPiecewiseObj(GurobiError):
    errno = 10026 
    argument = "Piecewise-linear objectives must have certain properties (as described in the documentation for the various setPWLObj methods). This error indicates that one of those properties was violated."


class GRBUpdatemodeChange(GurobiError):
    errno = 10027 
    argument = "The UpdateMode parameter can not be modified once a model has been created."


class GRBCloud(GurobiError):
    errno = 10028 
    argument = "Problems launching a Gurobi Instant Cloud job."


class GRBModelModification(GurobiError):
    errno = 10029 
    argument = "Indicates that the user has modified the model in such a way that the model became invalid. For example, this happens when a general constraint exists in the model and the user deletes the resultant variable of this constraint. In such a case, the general constraint does not have any meaningful interpretation anymore. The solution is to also delete the general constraint when a resultant variable is deleted."


class GRBCsworker(GurobiError):
    errno = 10030 
    argument = "When you are using a client-server feature, this error indicates that there was an application problem."


class GRBTuneModelTypes(GurobiError):
    errno = 10031 
    argument = "Indicates that tuning was invoked on a set of models, but the models were of different types (e.g., one an LP, another a MIP)."


class GRBSecurity(GurobiError):
    errno = 10032 
    argument = "Indicates that an authentication step failed or that an operation was attempted for which the current credentials do not warrant permission."


class GRBNotInModel(GurobiError):
    errno = 20001 
    argument = "Tried to use a constraint or variable that is not in the model, either because it was removed or because it has not yet been added."


class GRBFailedToCreateModel(GurobiError):
    errno = 20002 
    argument = "Failed to create the requested model"


class GRBInternal(GurobiError):
    errno = 20003 
    argument = "Internal Gurobi error"

codes_to_errors = {
    10001: GRBOutOfMemory,
    10002: GRBNullArgument,
    10003: GRBInvalidArgument,
    10004: GRBUnknownAttribute,
    10005: GRBDataNotAvailable,
    10006: GRBIndexOutOfRange,
    10007: GRBUnknownParameter,
    10008: GRBValueOutOfRange,
    10009: GRBNoLicense,
    10010: GRBSizeLimitExceeded,
    10011: GRBCallback,
    10012: GRBFileRead,
    10013: GRBFileWrite,
    10014: GRBNumeric,
    10015: GRBIisNotInfeasible,
    10016: GRBNotForMip,
    10017: GRBOptimizationInProgress,
    10018: GRBDuplicates,
    10019: GRBNodefile,
    10020: GRBQNotPsd,
    10021: GRBQcpEqualityConstraint,
    10022: GRBNetwork,
    10023: GRBJobRejected,
    10024: GRBNotSupported,
    10025: GRBExceed2bNonzeros,
    10026: GRBInvalidPiecewiseObj,
    10027: GRBUpdatemodeChange,
    10028: GRBCloud,
    10029: GRBModelModification,
    10030: GRBCsworker,
    10031: GRBTuneModelTypes,
    10032: GRBSecurity,
    20001: GRBNotInModel,
    20002: GRBFailedToCreateModel,
    20003: GRBInternal,
}

def raise_error(original_error):
    if isinstance(original_error, gp.GurobiError):
        raise codes_to_errors.get(original_error.errno, original_error)
    raise original_error
