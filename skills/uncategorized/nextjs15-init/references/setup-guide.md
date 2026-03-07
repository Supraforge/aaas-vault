# Next.js 15 Init 상세 가이드

## 전체 Setup 프로세스

### 1. 프로젝트 생성

**중요**: TypeScript, Tailwind CSS, App Router를 사용합니다.

```bash
npx create-next-app@latest my-app --typescript --tailwind --app --use-npm
cd my-app
```

**기본 설정**:
- TypeScript: 타입 안전성
- Tailwind CSS: 유틸리티 퍼스트 CSS
- App Router: Next.js 15의 최신 라우팅 시스템
- Package Manager: npm

### 2. package.json 기본 의존성

```json
{
  "name": "my-app",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "next": "^15.0.0"
  },
  "devDependencies": {
    "@types/node": "^20",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "typescript": "^5",
    "tailwindcss": "^3.4.1",
    "postcss": "^8",
    "autoprefixer": "^10.0.1",
    "eslint": "^8",
    "eslint-config-next": "^15.0.0"
  }
}
```

### 3. 폴더 구조 생성 스크립트

```bash
mkdir -p app/api
mkdir -p components/ui
mkdir -p components/layouts
mkdir -p lib/stores
mkdir -p lib/api
mkdir -p lib/validations
mkdir -p lib/utils
mkdir -p lib/db
```

**App Router 구조**:
```
app/
├── (auth)/            # 인증 관련 라우트 그룹
├── [domain]/          # 도메인별 페이지 (예: /todos, /blog)
├── api/[domain]/      # API 라우트
├── layout.tsx         # 루트 레이아웃
└── page.tsx           # 홈 페이지

components/
├── ui/                # ShadCN 컴포넌트
├── [domain]/          # 도메인별 컴포넌트
└── layouts/           # 레이아웃 컴포넌트

lib/
├── db/                # Prisma 클라이언트
├── stores/            # Zustand 스토어
├── api/               # API 클라이언트 로직
├── validations/       # Zod 스키마
└── utils/             # 유틸리티 함수
```

## 기본 파일 템플릿

### lib/utils.ts (shadcn 유틸리티)

```typescript
import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
```

### tailwind.config.ts

```typescript
import type { Config } from "tailwindcss"

const config: Config = {
  darkMode: ["class"],
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
}

export default config
```

### app/globals.css

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    --card: 0 0% 100%;
    --card-foreground: 222.2 84% 4.9%;
    --popover: 0 0% 100%;
    --popover-foreground: 222.2 84% 4.9%;
    --primary: 262.1 83.3% 57.8%;
    --primary-foreground: 210 40% 98%;
    --secondary: 210 40% 96.1%;
    --secondary-foreground: 222.2 47.4% 11.2%;
    --muted: 210 40% 96.1%;
    --muted-foreground: 215.4 16.3% 46.9%;
    --accent: 210 40% 96.1%;
    --accent-foreground: 222.2 47.4% 11.2%;
    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 210 40% 98%;
    --border: 214.3 31.8% 91.4%;
    --input: 214.3 31.8% 91.4%;
    --ring: 262.1 83.3% 57.8%;
    --radius: 0.5rem;
  }

  .dark {
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;
    --card: 222.2 84% 4.9%;
    --card-foreground: 210 40% 98%;
    --popover: 222.2 84% 4.9%;
    --popover-foreground: 210 40% 98%;
    --primary: 263.4 70% 50.4%;
    --primary-foreground: 210 40% 98%;
    --secondary: 217.2 32.6% 17.5%;
    --secondary-foreground: 210 40% 98%;
    --muted: 217.2 32.6% 17.5%;
    --muted-foreground: 215 20.2% 65.1%;
    --accent: 217.2 32.6% 17.5%;
    --accent-foreground: 210 40% 98%;
    --destructive: 0 62.8% 30.6%;
    --destructive-foreground: 210 40% 98%;
    --border: 217.2 32.6% 17.5%;
    --input: 217.2 32.6% 17.5%;
    --ring: 263.4 70% 50.4%;
  }
}

@layer base {
  * {
    @apply border-border;
  }
  body {
    @apply bg-background text-foreground;
  }
}
```

### components.json (ShadCN 설정)

```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "default",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.ts",
    "css": "app/globals.css",
    "baseColor": "slate",
    "cssVariables": true,
    "prefix": ""
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils"
  }
}
```

## ShadCN/ui 설치 및 구성

```bash
# ShadCN 초기화
npx shadcn@latest init

# 기본 컴포넌트 추가
npx shadcn@latest add button
npx shadcn@latest add card
npx shadcn@latest add input
npx shadcn@latest add form
npx shadcn@latest add table
npx shadcn@latest add dialog
npx shadcn@latest add dropdown-menu
npx shadcn@latest add select
npx shadcn@latest add checkbox
npx shadcn@latest add toast
```

## Essential 프리셋 패키지

```bash
npm install zustand
npm install @tanstack/react-query
npm install react-hook-form
npm install zod
npm install @hookform/resolvers
npm install lucide-react
npm install clsx tailwind-merge
npm install tailwindcss-animate
```

### lib/stores/example-store.ts (Zustand)

```typescript
import { create } from 'zustand'
import { devtools, persist } from 'zustand/middleware'

interface ExampleState {
  count: number
  increment: () => void
  decrement: () => void
  reset: () => void
}

export const useExampleStore = create<ExampleState>()(
  devtools(
    persist(
      (set) => ({
        count: 0,
        increment: () => set((state) => ({ count: state.count + 1 })),
        decrement: () => set((state) => ({ count: state.count - 1 })),
        reset: () => set({ count: 0 }),
      }),
      {
        name: 'example-storage',
      }
    )
  )
)
```

### app/providers.tsx (Tanstack Query)

```typescript
'use client'

import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { ReactQueryDevtools } from '@tanstack/react-query-devtools'
import { useState } from 'react'

export function Providers({ children }: { children: React.ReactNode }) {
  const [queryClient] = useState(
    () =>
      new QueryClient({
        defaultOptions: {
          queries: {
            staleTime: 60 * 1000, // 1분
            refetchOnWindowFocus: false,
          },
        },
      })
  )

  return (
    <QueryClientProvider client={queryClient}>
      {children}
      <ReactQueryDevtools initialIsOpen={false} />
    </QueryClientProvider>
  )
}
```

### app/layout.tsx (업데이트)

```typescript
import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'
import { Providers } from './providers'
import { Toaster } from '@/components/ui/toaster'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'My App',
  description: 'Next.js 15 App with ShadCN, Zustand, and Tanstack Query',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Providers>
          {children}
          <Toaster />
        </Providers>
      </body>
    </html>
  )
}
```

## 도메인별 보일러플레이트

### Todo 도메인 (완전한 예제)

#### lib/validations/todo.ts

```typescript
import { z } from 'zod'

export const todoSchema = z.object({
  id: z.number().optional(),
  title: z.string().min(1, 'Title is required'),
  description: z.string().optional(),
  completed: z.boolean().default(false),
  createdAt: z.date().optional(),
  updatedAt: z.date().optional(),
})

export type Todo = z.infer<typeof todoSchema>

export const createTodoSchema = todoSchema.omit({ id: true, createdAt: true, updatedAt: true })
export const updateTodoSchema = todoSchema.partial().required({ id: true })
```

#### lib/stores/todo-store.ts

```typescript
import { create } from 'zustand'
import { devtools, persist } from 'zustand/middleware'
import type { Todo } from '@/lib/validations/todo'

export type TodoFilter = 'all' | 'active' | 'completed'

interface TodoState {
  todos: Todo[]
  filter: TodoFilter
  setTodos: (todos: Todo[]) => void
  addTodo: (todo: Todo) => void
  updateTodo: (id: number, updates: Partial<Todo>) => void
  deleteTodo: (id: number) => void
  toggleTodo: (id: number) => void
  setFilter: (filter: TodoFilter) => void
  getFilteredTodos: () => Todo[]
}

export const useTodoStore = create<TodoState>()(
  devtools(
    persist(
      (set, get) => ({
        todos: [],
        filter: 'all',
        setTodos: (todos) => set({ todos }),
        addTodo: (todo) => set((state) => ({ todos: [...state.todos, todo] })),
        updateTodo: (id, updates) =>
          set((state) => ({
            todos: state.todos.map((todo) =>
              todo.id === id ? { ...todo, ...updates } : todo
            ),
          })),
        deleteTodo: (id) =>
          set((state) => ({
            todos: state.todos.filter((todo) => todo.id !== id),
          })),
        toggleTodo: (id) =>
          set((state) => ({
            todos: state.todos.map((todo) =>
              todo.id === id ? { ...todo, completed: !todo.completed } : todo
            ),
          })),
        setFilter: (filter) => set({ filter }),
        getFilteredTodos: () => {
          const { todos, filter } = get()
          if (filter === 'active') return todos.filter((t) => !t.completed)
          if (filter === 'completed') return todos.filter((t) => t.completed)
          return todos
        },
      }),
      {
        name: 'todo-storage',
      }
    )
  )
)
```

#### lib/api/todos.ts

```typescript
import type { Todo } from '@/lib/validations/todo'

const API_BASE = '/api/todos'

export async function getTodos(): Promise<Todo[]> {
  const res = await fetch(API_BASE)
  if (!res.ok) throw new Error('Failed to fetch todos')
  return res.json()
}

export async function getTodo(id: number): Promise<Todo> {
  const res = await fetch(`${API_BASE}/${id}`)
  if (!res.ok) throw new Error('Failed to fetch todo')
  return res.json()
}

export async function createTodo(data: Omit<Todo, 'id'>): Promise<Todo> {
  const res = await fetch(API_BASE, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  if (!res.ok) throw new Error('Failed to create todo')
  return res.json()
}

export async function updateTodo(id: number, data: Partial<Todo>): Promise<Todo> {
  const res = await fetch(`${API_BASE}/${id}`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  if (!res.ok) throw new Error('Failed to update todo')
  return res.json()
}

export async function deleteTodo(id: number): Promise<void> {
  const res = await fetch(`${API_BASE}/${id}`, {
    method: 'DELETE',
  })
  if (!res.ok) throw new Error('Failed to delete todo')
}
```

#### app/api/todos/route.ts

```typescript
import { NextRequest, NextResponse } from 'next/server'
import { todoSchema } from '@/lib/validations/todo'

// 메모리 스토리지 (Prisma 사용 시 DB로 교체)
let todos = [
  { id: 1, title: 'Example Todo', description: 'This is an example', completed: false, createdAt: new Date(), updatedAt: new Date() },
]
let nextId = 2

export async function GET() {
  return NextResponse.json(todos)
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json()
    const validated = todoSchema.omit({ id: true }).parse(body)

    const newTodo = {
      id: nextId++,
      ...validated,
      createdAt: new Date(),
      updatedAt: new Date(),
    }

    todos.push(newTodo)
    return NextResponse.json(newTodo, { status: 201 })
  } catch (error) {
    return NextResponse.json({ error: 'Invalid request' }, { status: 400 })
  }
}
```

#### app/api/todos/[id]/route.ts

**중요**: Next.js 15부터 `params`는 `Promise`로 변경되었습니다. 반드시 `await`로 해제해야 합니다.

```typescript
import { NextRequest, NextResponse } from 'next/server'

export async function GET(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  const { id: idStr } = await params
  const id = parseInt(idStr)
  const todo = todos.find((t) => t.id === id)

  if (!todo) {
    return NextResponse.json({ error: 'Todo not found' }, { status: 404 })
  }

  return NextResponse.json(todo)
}

export async function PATCH(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  const { id: idStr } = await params
  const id = parseInt(idStr)
  const todoIndex = todos.findIndex((t) => t.id === id)

  if (todoIndex === -1) {
    return NextResponse.json({ error: 'Todo not found' }, { status: 404 })
  }

  const body = await request.json()
  const updatedTodo = {
    ...todos[todoIndex],
    ...body,
    updatedAt: new Date(),
  }

  todos[todoIndex] = updatedTodo
  return NextResponse.json(updatedTodo)
}

export async function DELETE(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  const { id: idStr } = await params
  const id = parseInt(idStr)
  const todoIndex = todos.findIndex((t) => t.id === id)

  if (todoIndex === -1) {
    return NextResponse.json({ error: 'Todo not found' }, { status: 404 })
  }

  todos.splice(todoIndex, 1)
  return NextResponse.json({ message: 'Todo deleted' })
}
```

#### components/todos/todo-list.tsx

```typescript
'use client'

import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { getTodos, deleteTodo, updateTodo } from '@/lib/api/todos'
import { useTodoStore } from '@/lib/stores/todo-store'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Checkbox } from '@/components/ui/checkbox'
import { Trash2, Edit } from 'lucide-react'

export function TodoList() {
  const queryClient = useQueryClient()
  const filter = useTodoStore((state) => state.filter)

  const { data: todos = [], isLoading } = useQuery({
    queryKey: ['todos'],
    queryFn: getTodos,
  })

  const deleteMutation = useMutation({
    mutationFn: deleteTodo,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['todos'] })
    },
  })

  const toggleMutation = useMutation({
    mutationFn: ({ id, completed }: { id: number; completed: boolean }) =>
      updateTodo(id, { completed }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['todos'] })
    },
  })

  const filteredTodos = todos.filter((todo) => {
    if (filter === 'active') return !todo.completed
    if (filter === 'completed') return todo.completed
    return true
  })

  if (isLoading) return <div>Loading...</div>

  return (
    <div className="space-y-4">
      {filteredTodos.map((todo) => (
        <Card key={todo.id}>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <div className="flex items-center space-x-2">
              <Checkbox
                checked={todo.completed}
                onCheckedChange={(checked) =>
                  toggleMutation.mutate({ id: todo.id!, completed: !!checked })
                }
              />
              <CardTitle className={todo.completed ? 'line-through' : ''}>
                {todo.title}
              </CardTitle>
            </div>
            <div className="flex space-x-2">
              <Button variant="ghost" size="icon">
                <Edit className="h-4 w-4" />
              </Button>
              <Button
                variant="ghost"
                size="icon"
                onClick={() => deleteMutation.mutate(todo.id!)}
              >
                <Trash2 className="h-4 w-4" />
              </Button>
            </div>
          </CardHeader>
          {todo.description && (
            <CardContent>
              <p className="text-sm text-muted-foreground">{todo.description}</p>
            </CardContent>
          )}
        </Card>
      ))}
    </div>
  )
}
```

#### components/todos/todo-form.tsx

```typescript
'use client'

import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { useMutation, useQueryClient } from '@tanstack/react-query'
import { createTodoSchema } from '@/lib/validations/todo'
import { createTodo } from '@/lib/api/todos'
import { Button } from '@/components/ui/button'
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/components/ui/form'
import { Input } from '@/components/ui/input'
import { useToast } from '@/components/ui/use-toast'

export function TodoForm() {
  const queryClient = useQueryClient()
  const { toast } = useToast()

  const form = useForm({
    resolver: zodResolver(createTodoSchema),
    defaultValues: {
      title: '',
      description: '',
      completed: false,
    },
  })

  const createMutation = useMutation({
    mutationFn: createTodo,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['todos'] })
      form.reset()
      toast({
        title: 'Success',
        description: 'Todo created successfully',
      })
    },
    onError: () => {
      toast({
        title: 'Error',
        description: 'Failed to create todo',
        variant: 'destructive',
      })
    },
  })

  const onSubmit = form.handleSubmit((data) => {
    createMutation.mutate(data)
  })

  return (
    <Form {...form}>
      <form onSubmit={onSubmit} className="space-y-4">
        <FormField
          control={form.control}
          name="title"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Title</FormLabel>
              <FormControl>
                <Input placeholder="Enter todo title" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="description"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Description</FormLabel>
              <FormControl>
                <Input placeholder="Enter description (optional)" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <Button type="submit" disabled={createMutation.isPending}>
          {createMutation.isPending ? 'Creating...' : 'Add Todo'}
        </Button>
      </form>
    </Form>
  )
}
```

#### components/todos/todo-filter.tsx

```typescript
'use client'

import { useTodoStore, type TodoFilter } from '@/lib/stores/todo-store'
import { Button } from '@/components/ui/button'

export function TodoFilterBar() {
  const { filter, setFilter } = useTodoStore()

  const filters: { value: TodoFilter; label: string }[] = [
    { value: 'all', label: 'All' },
    { value: 'active', label: 'Active' },
    { value: 'completed', label: 'Completed' },
  ]

  return (
    <div className="flex space-x-2">
      {filters.map((f) => (
        <Button
          key={f.value}
          variant={filter === f.value ? 'default' : 'outline'}
          onClick={() => setFilter(f.value)}
        >
          {f.label}
        </Button>
      ))}
    </div>
  )
}
```

#### app/todos/page.tsx

```typescript
import { TodoList } from '@/components/todos/todo-list'
import { TodoForm } from '@/components/todos/todo-form'
import { TodoFilterBar } from '@/components/todos/todo-filter'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'

export default function TodosPage() {
  return (
    <div className="container mx-auto py-10">
      <div className="grid gap-6 md:grid-cols-[1fr_300px]">
        <div>
          <div className="mb-4 flex items-center justify-between">
            <h1 className="text-3xl font-bold">Todos</h1>
            <TodoFilterBar />
          </div>
          <TodoList />
        </div>
        <Card>
          <CardHeader>
            <CardTitle>Add New Todo</CardTitle>
          </CardHeader>
          <CardContent>
            <TodoForm />
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
```

---

## 선택 가능한 고급 기능

### 옵션 1: Drizzle ORM (TypeScript-first 데이터베이스 ORM)

#### 설치 (PostgreSQL)

```bash
npm install drizzle-orm postgres
npm install -D drizzle-kit
```

#### 설치 (SQLite)

```bash
npm install drizzle-orm better-sqlite3
npm install -D drizzle-kit @types/better-sqlite3
```

**중요**: SQLite를 사용하는 경우 next.config.js에 다음을 추가해야 합니다:

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  serverExternalPackages: ['better-sqlite3'],
}

module.exports = nextConfig
```

#### lib/db/schema.ts (PostgreSQL)

```typescript
import { pgTable, serial, text, boolean, timestamp } from 'drizzle-orm/pg-core'

export const todos = pgTable('todos', {
  id: serial('id').primaryKey(),
  title: text('title').notNull(),
  description: text('description'),
  completed: boolean('completed').default(false).notNull(),
  createdAt: timestamp('created_at').defaultNow().notNull(),
  updatedAt: timestamp('updated_at').defaultNow().notNull(),
})

export const posts = pgTable('posts', {
  id: serial('id').primaryKey(),
  title: text('title').notNull(),
  content: text('content').notNull(),
  excerpt: text('excerpt'),
  slug: text('slug').unique().notNull(),
  published: boolean('published').default(false).notNull(),
  createdAt: timestamp('created_at').defaultNow().notNull(),
  updatedAt: timestamp('updated_at').defaultNow().notNull(),
})

export type Todo = typeof todos.$inferSelect
export type NewTodo = typeof todos.$inferInsert
export type Post = typeof posts.$inferSelect
export type NewPost = typeof posts.$inferInsert
```

#### lib/db/schema.ts (SQLite)

```typescript
import { sqliteTable, integer, text } from 'drizzle-orm/sqlite-core'

export const todos = sqliteTable('todos', {
  id: integer('id').primaryKey({ autoIncrement: true }),
  title: text('title').notNull(),
  description: text('description'),
  completed: integer('completed', { mode: 'boolean' }).default(false).notNull(),
  createdAt: integer('created_at', { mode: 'timestamp' }).notNull().$defaultFn(() => new Date()),
  updatedAt: integer('updated_at', { mode: 'timestamp' }).notNull().$defaultFn(() => new Date()),
})

export type Todo = typeof todos.$inferSelect
export type NewTodo = typeof todos.$inferInsert
```

#### lib/db/index.ts (PostgreSQL)

```typescript
import { drizzle } from 'drizzle-orm/postgres-js'
import postgres from 'postgres'
import * as schema from './schema'

const connectionString = process.env.DATABASE_URL!

// Disable prefetch as it is not supported for "Transaction" pool mode
const client = postgres(connectionString, { prepare: false })

export const db = drizzle(client, { schema })
```

#### lib/db/index.ts (SQLite)

```typescript
import { drizzle } from 'drizzle-orm/better-sqlite3'
import Database from 'better-sqlite3'
import * as schema from './schema'
import { join } from 'path'

const sqlite = new Database(join(process.cwd(), 'app.db'))

export const db = drizzle(sqlite, { schema })
```

#### drizzle.config.ts (PostgreSQL)

```typescript
import type { Config } from 'drizzle-kit'

export default {
  schema: './lib/db/schema.ts',
  out: './drizzle',
  driver: 'pg',
  dbCredentials: {
    connectionString: process.env.DATABASE_URL!,
  },
} satisfies Config
```

#### drizzle.config.ts (SQLite)

```typescript
import type { Config } from 'drizzle-kit'

export default {
  schema: './lib/db/schema.ts',
  out: './drizzle',
  driver: 'better-sqlite',
  dbCredentials: {
    url: './app.db',
  },
} satisfies Config
```

#### Drizzle로 API 라우트 업데이트

```typescript
// app/api/todos/route.ts
import { NextRequest, NextResponse } from 'next/server'
import { db } from '@/lib/db'
import { todos } from '@/lib/db/schema'
import { todoSchema } from '@/lib/validations/todo'
import { desc } from 'drizzle-orm'

export async function GET() {
  const allTodos = await db.select().from(todos).orderBy(desc(todos.createdAt))
  return NextResponse.json(allTodos)
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json()
    const validated = todoSchema.omit({ id: true }).parse(body)

    const [newTodo] = await db
      .insert(todos)
      .values(validated)
      .returning()

    return NextResponse.json(newTodo, { status: 201 })
  } catch (error) {
    return NextResponse.json({ error: 'Invalid request' }, { status: 400 })
  }
}
```

#### 마이그레이션 실행 (PostgreSQL)

```bash
# 마이그레이션 파일 생성
npx drizzle-kit generate:pg

# 마이그레이션 실행
npx drizzle-kit push:pg

# Drizzle Studio 실행 (옵션)
npx drizzle-kit studio
```

#### 마이그레이션 실행 (SQLite)

```bash
# 마이그레이션 파일 생성
npx drizzle-kit generate:sqlite

# 마이그레이션 실행
npx drizzle-kit push:sqlite

# better-sqlite3 네이티브 바인딩 재빌드 (필요 시)
npm rebuild better-sqlite3

# Drizzle Studio 실행 (옵션)
npx drizzle-kit studio
```

**중요**: SQLite를 사용하는 경우, better-sqlite3의 네이티브 바인딩 문제가 발생할 수 있습니다. 빌드 실패 시 `npm rebuild better-sqlite3`를 실행하세요.

### 옵션 2: Better Auth (TypeScript-first 인증)

#### 설치

```bash
npm install better-auth
npm install bcryptjs
npm install -D @types/bcryptjs
```

#### lib/auth/auth.ts

```typescript
import { betterAuth } from 'better-auth'
import { db } from '@/lib/db'
import { drizzleAdapter } from 'better-auth/adapters/drizzle'

export const auth = betterAuth({
  database: drizzleAdapter(db, {
    provider: 'pg',
  }),
  emailAndPassword: {
    enabled: true,
  },
  socialProviders: {
    // 필요 시 소셜 로그인 추가
    // google: {
    //   clientId: process.env.GOOGLE_CLIENT_ID!,
    //   clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
    // },
  },
})

export type Session = typeof auth.$Infer.Session
```

#### lib/db/schema.ts (Auth 테이블 추가)

```typescript
import { pgTable, serial, text, boolean, timestamp } from 'drizzle-orm/pg-core'

// 기존 테이블들...

// Better Auth 테이블
export const users = pgTable('users', {
  id: serial('id').primaryKey(),
  name: text('name'),
  email: text('email').unique().notNull(),
  emailVerified: boolean('email_verified').default(false),
  image: text('image'),
  createdAt: timestamp('created_at').defaultNow().notNull(),
  updatedAt: timestamp('updated_at').defaultNow().notNull(),
})

export const accounts = pgTable('accounts', {
  id: serial('id').primaryKey(),
  userId: serial('user_id').references(() => users.id, { onDelete: 'cascade' }),
  accountId: text('account_id').notNull(),
  providerId: text('provider_id').notNull(),
  accessToken: text('access_token'),
  refreshToken: text('refresh_token'),
  expiresAt: timestamp('expires_at'),
  password: text('password'), // 이메일/비밀번호 로그인용
})

export const sessions = pgTable('sessions', {
  id: serial('id').primaryKey(),
  userId: serial('user_id').references(() => users.id, { onDelete: 'cascade' }),
  token: text('token').unique().notNull(),
  expiresAt: timestamp('expires_at').notNull(),
  createdAt: timestamp('created_at').defaultNow().notNull(),
})

export const verificationTokens = pgTable('verification_tokens', {
  id: serial('id').primaryKey(),
  identifier: text('identifier').notNull(),
  token: text('token').unique().notNull(),
  expiresAt: timestamp('expires_at').notNull(),
})
```

#### app/api/auth/[...all]/route.ts

```typescript
import { auth } from '@/lib/auth/auth'

export const { GET, POST } = auth.handler
```

#### lib/auth/auth-client.ts

```typescript
import { createAuthClient } from 'better-auth/react'

export const authClient = createAuthClient({
  baseURL: process.env.NEXT_PUBLIC_APP_URL || 'http://localhost:3000',
})

export const { signIn, signUp, signOut, useSession } = authClient
```

#### middleware.ts

```typescript
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'
import { auth } from '@/lib/auth/auth'

export async function middleware(request: NextRequest) {
  const session = await auth.api.getSession({
    headers: request.headers,
  })

  const isAuthPage = request.nextUrl.pathname.startsWith('/login') ||
                     request.nextUrl.pathname.startsWith('/register')

  if (isAuthPage && session) {
    return NextResponse.redirect(new URL('/todos', request.url))
  }

  if (!isAuthPage && !session) {
    return NextResponse.redirect(new URL('/login', request.url))
  }

  return NextResponse.next()
}

export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)'],
}
```

#### app/login/page.tsx (예제)

```typescript
'use client'

import { useState } from 'react'
import { signIn } from '@/lib/auth/auth-client'
import { useRouter } from 'next/navigation'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'

export default function LoginPage() {
  const router = useRouter()
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()

    await signIn.email({
      email,
      password,
      callbackURL: '/todos',
    })

    router.push('/todos')
  }

  return (
    <div className="flex min-h-screen items-center justify-center">
      <form onSubmit={handleSubmit} className="w-full max-w-md space-y-4">
        <h1 className="text-2xl font-bold">Login</h1>
        <Input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <Input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <Button type="submit" className="w-full">
          Sign In
        </Button>
      </form>
    </div>
  )
}
```

### 옵션 3: Framer Motion (애니메이션)

#### 설치

```bash
npm install framer-motion
```

#### components/animated-card.tsx

```typescript
'use client'

import { motion } from 'framer-motion'
import { Card } from '@/components/ui/card'

export function AnimatedCard({ children, ...props }: React.ComponentProps<typeof Card>) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -20 }}
      transition={{ duration: 0.3 }}
    >
      <Card {...props}>{children}</Card>
    </motion.div>
  )
}
```

#### 사용 예제

```typescript
import { AnimatedCard } from '@/components/animated-card'

export function TodoList() {
  return (
    <div className="space-y-4">
      {todos.map((todo) => (
        <AnimatedCard key={todo.id}>
          {/* Todo content */}
        </AnimatedCard>
      ))}
    </div>
  )
}
```

## 코드 검증 및 오류 수정

### 1. ESLint 실행

```bash
npm run lint
```

### 2. 자주 발생하는 오류 및 해결 방법

#### Import 경로 오류
```typescript
// ❌ 잘못된 예
import { Button } from '../../../components/ui/button'

// ✅ 올바른 예 (tsconfig.json의 paths 사용)
import { Button } from '@/components/ui/button'
```

#### TypeScript 타입 오류
```typescript
// ❌ 타입 명시 없음
export async function GET(request) {
  // ...
}

// ✅ 타입 명시
export async function GET(request: NextRequest) {
  // ...
}
```

#### 클라이언트 컴포넌트 표시
```typescript
// useState, useEffect 등 React Hooks를 사용하는 컴포넌트는 반드시 'use client' 추가
'use client'

import { useState } from 'react'

export function MyComponent() {
  const [count, setCount] = useState(0)
  // ...
}
```

#### Next.js 15 Route Handler params 오류
```typescript
// ❌ Next.js 14 스타일 (빌드 실패)
export async function GET(
  request: NextRequest,
  { params }: { params: { id: string } }
) {
  const id = params.id  // Type error!
}

// ✅ Next.js 15 스타일 (params는 Promise)
export async function GET(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  const { id } = await params  // ✅ Correct!
}
```

#### SQLite (better-sqlite3) 빌드 오류
```bash
# 오류: Could not locate the bindings file
# 해결 방법 1: next.config.js 설정
const nextConfig = {
  serverExternalPackages: ['better-sqlite3'],
}

# 해결 방법 2: 네이티브 바인딩 재빌드
npm rebuild better-sqlite3
```

### 3. 성공 기준

✅ `npm run lint` 결과가 "0 errors"
✅ `npm run build` 또는 `pnpm build` 성공
✅ TypeScript 컴파일 성공
✅ 모든 import 경로 해결됨
✅ 'use client' 지시어가 적절히 사용됨
✅ Next.js 15 params Promise 패턴 사용

## Full Stack package.json

```json
{
  "dependencies": {
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "next": "^15.0.0",
    "@radix-ui/react-checkbox": "^1.0.4",
    "@radix-ui/react-dialog": "^1.0.5",
    "@radix-ui/react-dropdown-menu": "^2.0.6",
    "@radix-ui/react-label": "^2.0.2",
    "@radix-ui/react-select": "^2.0.0",
    "@radix-ui/react-slot": "^1.0.2",
    "@radix-ui/react-toast": "^1.1.5",
    "@tanstack/react-query": "^5.28.4",
    "@tanstack/react-query-devtools": "^5.28.4",
    "zustand": "^4.5.2",
    "react-hook-form": "^7.51.1",
    "zod": "^3.22.4",
    "@hookform/resolvers": "^3.3.4",
    "drizzle-orm": "^0.29.0",
    "postgres": "^3.4.3",
    "better-auth": "^0.8.0",
    "bcryptjs": "^2.4.3",
    "framer-motion": "^11.0.20",
    "lucide-react": "^0.358.0",
    "clsx": "^2.1.0",
    "tailwind-merge": "^2.2.2",
    "tailwindcss-animate": "^1.0.7",
    "class-variance-authority": "^0.7.0"
  },
  "devDependencies": {
    "@types/node": "^20",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "@types/bcryptjs": "^2.4.6",
    "drizzle-kit": "^0.20.0",
    "typescript": "^5",
    "tailwindcss": "^3.4.1",
    "postcss": "^8",
    "autoprefixer": "^10.0.1",
    "eslint": "^8",
    "eslint-config-next": "^15.0.0"
  }
}
```

## 환경 변수 (.env.local)

```env
# Database
DATABASE_URL="postgresql://user:password@localhost:5432/mydb"

# Better Auth
BETTER_AUTH_SECRET="your-secret-key-here"
BETTER_AUTH_URL="http://localhost:3000"
NEXT_PUBLIC_APP_URL="http://localhost:3000"
```

---

## 대화형 선택 가이드

사용자가 각 프리셋을 선택하면:

1. **Essential (권장)**: ShadCN, Zustand, React Hook Form + Zod 설치
2. **Minimal**: Next.js + TypeScript + Tailwind만 설치
3. **Full Stack**: 모든 기능 (Drizzle ORM, Better Auth, Framer Motion 포함) 설치
4. **Custom**: 각 기능을 개별적으로 선택

모든 선택은 독립적으로 작동하며, 원하는 조합으로 구성 가능합니다.

## 린트 설정 (ESLint)

Next.js 프로젝트는 기본적으로 **ESLint**를 사용합니다.

### 기본 설정 (.eslintrc.json)

```json
{
  "extends": "next/core-web-vitals"
}
```

### 린트 실행

```bash
# 린트 검사
npm run lint

# 린트 자동 수정
npm run lint -- --fix
```

### 추가 린트 규칙 (선택사항)

```json
{
  "extends": ["next/core-web-vitals", "next/typescript"],
  "rules": {
    "@typescript-eslint/no-unused-vars": "error",
    "@typescript-eslint/no-explicit-any": "warn",
    "prefer-const": "error",
    "no-console": ["warn", { "allow": ["warn", "error"] }]
  }
}
```

### Prettier 통합 (선택사항)

```bash
npm install -D prettier eslint-config-prettier
```

**.prettierrc**:
```json
{
  "semi": false,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5"
}
```

**.eslintrc.json** (업데이트):
```json
{
  "extends": ["next/core-web-vitals", "prettier"]
}
```
