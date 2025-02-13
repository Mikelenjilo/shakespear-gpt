import torch

def get_batch(split, batch_size=4, block_size=8, seed=1337):
    torch.manual_seed(1337)
    
    data = train_data if split == 'train' else val_data
    ix = torch.randint(len(data) - block_size, (batch_size,))
   
    x = torch.stack([data[i:i+block_size] for i in ix])
    y = torch.stack([data[i+1:i+block_size+1] for i in ix])

    return x, y