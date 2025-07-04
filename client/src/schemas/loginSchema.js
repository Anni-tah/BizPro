import {z} from 'zod';
 const loginSchema = z.object({
    email: z.string()
    .email('Invalid email address')
    .min(1, 'Email is required'),
    password: z
    .string()
    .min(8, 'Password must be at least 8 characters long')
    .regex(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/, 'Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character'),
    rememberMe: z.boolean().optional(),
});
export default loginSchema;


