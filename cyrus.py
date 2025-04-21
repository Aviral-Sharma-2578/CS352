import numpy as np
import matplotlib.pyplot as plt

def cyrus_beck_clip(P0, P1, polygon):
    """
    Clips the line segment from P0 to P1 against the convex polygon using the Cyrus-Beck algorithm.
    polygon: list of vertices in CCW order.
    Returns the clipped segment endpoints or None if rejected.
    """
    D = P1 - P0
    t_enter, t_leave = 0.0, 1.0
    # Compute inward normals for each edge
    for i in range(len(polygon)):
        Pi = polygon[i]
        Pj = polygon[(i + 1) % len(polygon)]
        E = Pj - Pi
        # Inward normal (for CCW polygon)
        N = np.array([E[1], -E[0]])
        W = P0 - Pi
        denom = N.dot(D)
        num = -N.dot(W)
        if np.isclose(denom, 0):
            # Parallel: if outside, reject
            if num < 0:
                return None
            else:
                continue
        t = num / denom
        if denom > 0:
            # Potential leaving point
            t_leave = min(t_leave, t)
        else:
            # Potential entering point
            t_enter = max(t_enter, t)
        if t_enter > t_leave:
            return None
    clipped_P0 = P0 + t_enter * D
    clipped_P1 = P0 + t_leave * D
    return clipped_P0, clipped_P1

# Define a convex polygon (window) in CCW order
polygon = np.array([
    [1, 1],
    [5, 2],
    [4, 5],
    [2, 4]
])

# Define a line segment to be clipped
P0 = np.array([0, 3])
P1 = np.array([6, 3])

# Perform clipping
clipped = cyrus_beck_clip(P0, P1, polygon)

# Plotting
fig, ax = plt.subplots()
# Polygon window
ax.plot(*np.vstack([polygon, polygon[0]]).T)
# Original line segment
ax.plot([P0[0], P1[0]], [P0[1], P1[1]], linestyle='--', label='Original Line')
# Clipped segment, if any
if clipped is not None:
    C0, C1 = clipped
    ax.plot([C0[0], C1[0]], [C0[1], C1[1]], linewidth=2, label='Clipped Segment')

ax.set_aspect('equal', 'box')
ax.legend()
ax.set_title('Cyrus-Beck Line Clipping')
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.show()
