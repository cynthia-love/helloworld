# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    思考动态数组扩展不是n-2n, 而是n->1.25n
    证明这种情况下, append操作的摊销时间复杂度还是O(1)

"""

"""
    分析: 0, 1, 2, 3, ...k...1.25k, 1.25k+1
    
    索引k处扩展到1.25k, 复制时间k
    成本摊销目标: 1.25k-1-k+1 = 0.25k
    
    每个目标摊销: k/0.25k = 4
    
    即平均每次append时间复杂度O(5n)
    
"""

"""
    用提前收费的思路呢
    1.25k用于收费的目标: k, k+1, ...1.25k-1 = 0.25k
    
    1.25k处复制耗时1.25k
    
    摊销到0.25k上每个5
    
    即平均每次append需要提前收取5个网络硬币的费用
    
    平均每次append的时间复杂度O(6n)

"""