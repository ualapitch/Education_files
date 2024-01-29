def recurrence_relation(n, m) -> int:
    """Return number of rabbits that will be present in n month with live time in m month"""
    m_b = 1
    ctr = 1
    m_bb = 1
    m_b_2 = 1
    m_bb_2 = 1
    while n-2 != 0:
        m_s = m_b
        m_b += m_bb
        m_bb = m_s
        print(m_b)
        if ctr <= m:
            pass
        else:
            m_s_2 = m_b_2
            m_b_2 += m_bb_2
            m_bb_2 = m_s_2
            m_b -= m_b_2
        ctr += 1
        n -= 1
    return m_b


print(recurrence_relation(6, 3))