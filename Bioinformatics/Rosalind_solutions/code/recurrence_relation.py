def recurrence_relation(n, k) -> int:
    """Return number of rabbits that will be present in n month with litter of k rabbit pairs"""
    m_b = 1 + k
    m_bb = 1
    while n-3 != 0:
        m_s = m_b
        m_b += m_bb*k
        m_bb = m_s
        n -= 1
    return m_b


print(recurrence_relation(35, 2))