import numpy as np

def leadlag(X):
  
  # if len(X.shape) == 1:
  lead = []
  lag = []
  for val_lag, val_lead in zip(X[:-1], X[1:]):
      lag.append(val_lag)
      lead.append(val_lag)

      lag.append(val_lag)
      lead.append(val_lead)

  lag.append(X[-1])
  lead.append(X[-1])
  leadlag = np.c_[lag, lead]
  
  # else:
  #   time_dim, num_assets = X.shape
  #   asset_1 = X[:, 0]
  #   lead = np.delete(np.repeat(asset_1, 2), 0).reshape(-1, 1)
  #   lag = np.delete(np.repeat(asset_1, 2), -1).reshape(-1, 1)
    
  #   for i in range(1, num_assets):
  #     asset_i = X[:, i]
  #     asset_i_lead = np.delete(np.repeat(asset_i, 2), 0).reshape(-1, 1)
  #     asset_i_lag = np.delete(np.repeat(asset_i, 2), -1).reshape(-1, 1)
  #     lead = np.concatenate((lead, asset_i_lead), axis=1)
  #     lag = np.concatenate((lag, asset_i_lag), axis=1)
  #   leadlag = np.concatenate((lag, lead), axis=1)
    
  return leadlag