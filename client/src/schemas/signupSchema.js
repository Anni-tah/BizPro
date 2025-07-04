import { z } from 'zod';

const signupSchema = z
  .object({
    username: z.string()
      .min(1, 'Username is required')
      .max(20, 'Username must be at most 20 characters long'),

    email: z.string()
      .email('Invalid email address')
      .min(1, 'Email is required'),

    role: z.enum(['admin', 'storekeeper', 'customer', 'supplier'], {
      required_error: 'Role is required',
      invalid_type_error: 'Invalid role selected',
    }),

    password: z.string()
      .min(8, 'Password must be at least 8 characters long')
      .regex(
        /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])/,
        'Password must contain an uppercase letter, lowercase letter, number, and special character'
      ),

    confirmPassword: z.string()
      .min(1, 'Confirm Password is required'),
  })
  .refine((data) => data.password === data.confirmPassword, {
    path: ['confirmPassword'],
    message: 'Passwords do not match',
  });

export default signupSchema;
