// Timestamp: 2025-11-06 01:07:31

type Omit<T, K extends keyof T> = Pick<T, Exclude<keyof T, K>>;

